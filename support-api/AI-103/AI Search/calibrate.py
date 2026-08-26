"""Pick the refusal threshold by measurement, not by feeling.

Runs the golden set on a range of thresholds and print where in-corpus and out-of-corpus
questions separate. (hint -> P2)"""

import json
from pathlib import Path

from kb_lib import query

GOLDEN = json.loads(
    (Path("corpus") / "golden-set.json").read_text(encoding="utf-8")
)

def top_score(question: str) -> float:
    """Retrieve once and return the best reranker score, or 0.0 for nothing."""
    result = query(question, source_data=True)
    scores = [r.reranker_score for r in (result.references or []) if r.reranker_score]
    return max(scores) if scores else 0.0

print("scoring the golden set...")
scored = []
for case in GOLDEN["cases"]:
    score = top_score(case["question"])
    scored.append((case, score))
    print(f"  {case['id']}  {score:5.2f}  expect={case['expect']:6}  {case['question'][:52]}")

answerable = [(c, s) for c, s in scored if c["expect"] == "answer"]
refusable = [(c, s) for c, s in scored if c["expect"] == "refuse"]
print(f"\n{'thresh':>7} {'answered':>9} {'wrongly refused':>16} {'wrongly answered':>17}") # titles for our table
print("-" * 54)
best = None
for step in range (0, 41): # reranker score goes to 4.0
    threshold = step * 0.1
    # a case is answered when its best reference clears the threshold
    missed = [c["id"] for c, s in answerable if s < threshold]
    leaked = [c["id"] for c, s in refusable if s >= threshold]
    print(f"{threshold:7.1f} {len(answerable) - len(missed):9} "
          f"{len(missed):16} {len(leaked):17}")
    if not missed and not leaked and best is None: 
        best = threshold

print()
if best is None:
    print("NO CLEAN SEPARATION - the corpus and the golden set overlap.")
    print("That is a finding, not a failure. Report the least-bad threshold and")
    print("the cases it gets wrong, rather than pretending a clean value exists.")
else:
    lowest_answer = min(s for _, s in answerable)
    highest_refuse = max(s for _, s in refusable) if refusable else 0.0
    print(f"lowest in-corpus score   : {lowest_answer:.2f}")
    print(f"highest out-of-corpus    : {highest_refuse:.2f}")
    print(f"clean separation from    : {best:.1f}")
    print(f"recommended threshold    : {(lowest_answer + highest_refuse) / 2:.2f}"
          "  (midpoint of the gap)")
    print("score used               : @search.rerankerScore (semantic ranker,")
    print("                           bounded 0-4, NOT @search.score)")