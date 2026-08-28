"""Does a HyDE draft push an OUT-OF-CORPUS question past the threshold (TAU)?"""

import json

from attacks import hyde_draft
from guardrails import TAU
from kb_tool import retrieve

GOLDEN = json.loads(open("corpus/golden-set.json", encoding="utf-8").read())
REFUSE = [c for c in GOLDEN["cases"] if c["expect"] == "refuse"] # gets all refusal cases

def top(q: str) -> float:
    return max((r["reranker"] or 0 for r in retrieve(q, k=5)), default=0.0)

print(f"tau = {TAU}     |       scoring what reaches the gate, not the question\n")
for case in REFUSE:
    base = top(case["question"])
    drafts = [top(hyde_draft(case["question"])) for _ in range(3)]
    hi = max(drafts)
    flag = "     *** CROSSES TAU ***" if hi >= TAU else ""
    print(f"{case['id']}  verbatim={base:.2f}  HyDE best={hi:.2f}  ({hi - base:+.2f}){flag}")
