"""The TAU (threshold) filter ruined our second hop (G01). Does a compression method do the same?"""

from attacks import _ask
from guardrails import TAU
from kb_tool import retrieve

Q = "Does rotating a TLS certificate on a load balancer need CAB approval?"
WANT = {"CHG-CAT", "CHG-STD"}

COMPRESS_PROMPT = (
    "Extract ONLY the sentences from the passage below that help answer the "
    "question. Copy them verbatim. If none of the passage is relevant, reply "
    "with exactly NONE.\n\n"
)

rows = retrieve(Q, k=5)
for run in range(1, 4):
    survivors, before, after = [], 0, 0
    for r in rows:
        before += len(r["content"])
        out = (_ask(COMPRESS_PROMPT + f"Question: {Q}\n\nPassage:\n{r['content']}") or "").strip()
        if out.upper().startswith("NONE") or not out:
            continue
        after += len(out)
        survivors.append(r["doc_id"])
    lost = WANT - set(survivors)
    pct = 100 - (after * 100 // before)
    print(f"run {run}: {before} -> {after} chars ({pct}% smaller), "
          f"{len(rows)}->{len(survivors)} chunks, docs {sorted(set(survivors))}  "
          f"*** {'BOTH SURVIVE' if not lost else f'LOST {sorted(lost)}'} ***")