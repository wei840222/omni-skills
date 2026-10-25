"""Grader canaries only: these are not baseline/challenger agent task outputs."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from harness_task_checks import public_task_input, run_task_check

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "experiments/fixtures/harness_task_checks.json"

# Small authored acceptance controls. Never send these to the task-solving models.
GOOD = {
    "t01": 'export type Result={ok:true,value:number}|{ok:false,message:string};\nexport function describe(r:Result):string{return r.ok ? "value="+r.value : "error="+r.message;}',
    "t02": 'export function pick<T extends object,K extends keyof T>(o:T,k:K):T[K]{return o[k];}',
    "t03": 'function makeReaders(items){return items.map(item=>()=>item);}',
    "t04": 'function uniqueById(rows){const seen=new Set();return rows.filter(row=>{if(seen.has(row.id))return false;seen.add(row.id);return true;});}',
    "t05": 'BEGIN IMMEDIATE; UPDATE accounts SET balance=balance-(SELECT amount FROM request) WHERE id=(SELECT sender FROM request); UPDATE accounts SET balance=balance+(SELECT amount FROM request) WHERE id=(SELECT recipient FROM request); INSERT INTO ledger SELECT sender,recipient,amount FROM request; COMMIT;',
    "t06": 'WITH ranked AS (SELECT customer,event_id,SUM(amount) OVER (PARTITION BY customer) AS total,ROW_NUMBER() OVER (PARTITION BY customer ORDER BY occurred_at DESC,event_id DESC) AS n FROM events) SELECT customer,event_id,total FROM ranked WHERE n=1 ORDER BY customer;',
    "t07": 'def convert_csv(text):\n    rows=list(csv.reader(io.StringIO(text),delimiter=";"))\n    out=io.StringIO(newline="")\n    csv.writer(out,lineterminator="\\r\\n").writerows(rows)\n    return out.getvalue()\n',
    "t08": 'def summarize(records):\n    if not records: return []\n    frame=pd.DataFrame(records)\n    frame["units"]=frame["units"].fillna(0).astype(int)\n    return frame.groupby("sku",sort=True,as_index=False)["units"].sum().to_dict("records")\n',
    "t09": 'emit_argv() { if [ "$#" -gt 0 ]; then printf \'%s\\0\' "$@"; fi; }',
    "t10": 'basenames() { while IFS= read -r -d \'\' part; do printf \'%s\\0\' "${part##*/}"; done; }',
    "t11": json.dumps({"pattern": r"(?<![A-Za-z0-9_])[A-Z]{2,5}-[0-9]{1,6}(?![A-Za-z0-9_])", "flags": "g"}),
    "t12": 'def parse_records(text):\n    out=[]\n    seen=set()\n    for line in text.splitlines():\n        if not line.strip(): continue\n        row=json.loads(line)\n        if type(row) is not dict or set(row)!={"id","value"}: raise ValueError()\n        if type(row["id"]) is not str or not row["id"].strip() or type(row["value"]) is not int or row["id"] in seen: raise ValueError()\n        seen.add(row["id"])\n        out.append(row)\n    return out\n',
}
BAD = {
    "t01": 'export type Result={ok:true,value:number}|{ok:false,message:string}; export function describe(r:Result):string{return "value="+r.value;}',
    "t02": 'export function pick(o:{[key:string]:string|number},k:string):string|number{return o[k];}',
    "t03": 'function makeReaders(items){var out=[];for(var i=0;i<items.length;i++){out.push(()=>items[i]);}return out;}',
    "t04": 'function uniqueById(rows){return rows.reverse();}',
    "t05": GOOD["t05"].replace("BEGIN IMMEDIATE;", "").replace("COMMIT;", ""),
    "t06": 'SELECT customer,MAX(event_id) AS event_id,SUM(amount) AS total FROM events GROUP BY customer ORDER BY customer;',
    "t07": 'def convert_csv(text):\n    return text.replace(";",",")\n',
    "t08": 'def summarize(records):\n    return records\n',
    "t09": 'emit_argv() { printf \'%s\\0\' $@; }',
    "t10": 'basenames() { while read part; do printf \'%s\\0\' "$part"; done; }',
    "t11": json.dumps({"pattern": ".*", "flags": "g"}),
    "t12": 'def parse_records(text):\n    return json.loads(text)\n',
}


class TaskCheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec = json.loads(FIXTURE.read_text())
        cls.tasks = {task["id"]: task for task in cls.spec["tasks"]}
        cls.parent = ROOT / "experiments/datasets/task-check-test-fixtures"
        cls.parent.mkdir(parents=True, exist_ok=True)

    def check_source(self, task_id, source):
        with tempfile.TemporaryDirectory(dir=self.parent) as folder:
            filename = Path(folder) / self.tasks[task_id]["public"]["artifact_contract"]["filename"]
            filename.write_text(source)
            return run_task_check(task_id, folder)

    def test_authored_acceptance_controls_pass(self):
        for task_id, source in GOOD.items():
            with self.subTest(task_id=task_id):
                result = self.check_source(task_id, source)
                self.assertTrue(result["passed"], result)
                self.assertTrue(result["checks"])
                self.assertFalse(result["failures"])

    def test_each_distinct_wrong_behavior_is_rejected(self):
        for task_id, source in BAD.items():
            with self.subTest(task_id=task_id):
                result = self.check_source(task_id, source)
                self.assertFalse(result["passed"], result)
                self.assertTrue(result["failures"])

    def test_public_projection_never_contains_grader_or_source_owner(self):
        self.assertEqual(len(self.tasks), 12)
        for task_id in self.tasks:
            view = public_task_input(task_id)
            self.assertEqual(set(view), {"id", "request", "artifact_contract", "input_data"})
            self.assertNotIn("grader", view)
            self.assertNotIn("source_refs", view)
            view["request"] = "mutated copy"
            self.assertNotEqual(public_task_input(task_id)["request"], "mutated copy")

    def test_suppression_import_and_external_path_are_rejected(self):
        for task_id, source in [("t01", "// @ts-nocheck\n" + GOOD["t01"]),
                                ("t12", "import os\n" + GOOD["t12"]),
                                ("t09", "emit_argv() { eval \"$@\"; }")]:
            self.assertFalse(self.check_source(task_id, source)["passed"])
        with self.assertRaises(ValueError):
            run_task_check("t01", ROOT / "skills")

    def test_runtime_checks_reject_type_safe_wrong_property_and_live_closures(self):
        wrong_property = GOOD["t02"].replace("return o[k]", "return Object.values(o)[0]")
        result = self.check_source("t02", wrong_property)
        self.assertTrue(result["checks"][0]["passed"], result)
        self.assertFalse(result["passed"])
        live_readers = "function makeReaders(items){return items.map((item,index)=>()=>items[index]);}"
        self.assertFalse(self.check_source("t03", live_readers)["passed"])

    def test_submitted_runtime_has_no_grader_expected_results(self):
        oracle_reader = "function uniqueById(rows){const p=JSON.parse(dataJSON);return p.grader.cases.find(c=>JSON.stringify(c.args[0])===JSON.stringify(rows)).expected;}"
        self.assertFalse(self.check_source("t04", oracle_reader)["passed"])

    def test_frozen_inputs_sources_and_validator_files(self):
        freeze = self.spec["freeze"]
        self.assertIsNotNone(freeze)
        for task in self.tasks.values():
            for ref in task["source_refs"]:
                self.assertEqual(hashlib.sha256((ROOT / ref["path"]).read_bytes()).hexdigest(), ref["sha256"])
        for source in freeze["files"]:
            self.assertEqual(hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest(), source["sha256"])


if __name__ == "__main__":
    unittest.main()
