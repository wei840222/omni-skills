# Prompt failure diagnosis

Start with the original failing input, the expected result, the deployed model/version, and the observed output. Change one causal variable, then re-run the same case and regression set.

| Failure | Evidence | First correction | If it persists |
|---|---|---|---|
| Unsupported or invented claims | Output contains facts absent from the supplied source material | Delimit the permitted source material and require uncertainty to be reported explicitly | Verify retrieval, source coverage, and model/tool configuration before changing wording again |
| Invalid or incomplete structured output | Schema validation fails or required fields are missing | State the schema and required fields; use the platform's structured-output feature when available | Validate the returned value before downstream use and reduce conflicting output instructions |
| Instruction drift | A required constraint is absent despite being supplied | Move the measurable constraint into the task and output-contract sections | Shorten competing instructions and add a representative evaluation case |
| Legitimate request is misunderstood | The response declines or answers a different task | State the legitimate objective, available authority, and bounded deliverable | Separate the request into a safe, independently evaluable subtask |
| Excess verbosity | Output exceeds the stated length or format | Specify a measurable word, character, or item limit | Add a passing short-form example and test the limit automatically where possible |
| Superficial alternatives | Candidates differ only in wording | Name distinct variation axes such as structure, audience framing, or emotional angle | Require one candidate per axis and compare them against the requested purpose |
| Voice drift | Part of the response no longer matches supplied samples | Extract observable style patterns and check the complete output against them | Add a representative sample and evaluate paragraph-level consistency |

Use `references/models.md` when the failure begins after a model or platform change. Use `references/iteration.md` to run the corrective experiment.
