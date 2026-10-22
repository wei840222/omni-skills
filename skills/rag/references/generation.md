# Generation — cite or refuse

**Load when** answers ignore mid-context facts, cite nothing, or hallucinate over good retrieval.

- Under `answer_policy: cite-or-refuse`, every claim cites a chunk id that is present in the retrieved set; verify ids in code.
- When the top score sits below the corpus-calibrated refusal floor, say the corpus does not cover it.
- Mid-context material is used least (Liu et al., *Lost in the Middle*—`references/sources.md`). Prefer putting the strongest evidence first/last, or compress.
- Delimit retrieved content as data. Never let indexed text carry instructions into the generator.
