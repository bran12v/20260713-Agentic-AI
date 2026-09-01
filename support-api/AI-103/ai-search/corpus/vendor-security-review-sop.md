# Vendor Security Review SOP

**Doc id:** VND-SOP
**Doc type:** sop
**Owner:** Information Security
**Effective:** 2026-01-10

## 1. When a review is required

A vendor security review is required before a vendor is granted any production
access under ACC-POL, before a vendor-supplied component is deployed to
production, and before client data is transmitted to a vendor by any route.

A review is also required on renewal, on a material change to the service the
vendor provides, and on notification of a security incident at the vendor.

## 2. Vendor tiers

Tier is assigned by Information Security at intake from the vendor's data access
and its position in the client-facing path. Tier drives the depth of review and
the review interval.

| Tier | Definition | Review depth | Interval | Approver |
|---|---|---|---|---|
| Tier 1 | Processes or stores client data | Full assessment, evidence review, penetration test report, on-site or virtual audit | 12 months | Information Security + sponsoring director |
| Tier 2 | Production access without client data access | Full assessment, evidence review, penetration test report | 24 months | Information Security |
| Tier 3 | In the client-facing path, no data or access | Questionnaire, certification review | 24 months | Information Security |
| Tier 4 | No production involvement | Questionnaire only | 36 months | Service owner |

A vendor is assigned the highest tier for which it qualifies on any engagement. A
vendor operating at Tier 3 for one service and Tier 1 for another is reviewed as
Tier 1 across the relationship — tier attaches to the vendor, not to the
engagement.

## 3. Assessment components

| Component | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Security questionnaire | Yes | Yes | Yes | Yes |
| Current certification (ISO 27001 or SOC 2 Type II) | Yes | Yes | Yes | No |
| Penetration test report, within 12 months | Yes | Yes | No | No |
| Evidence review of stated controls | Yes | Yes | No | No |
| Subprocessor disclosure | Yes | Yes | Yes | No |
| Incident notification undertaking | Yes | Yes | Yes | No |
| Audit, on-site or virtual | Yes | No | No | No |
| Data residency attestation | Yes | No | No | No |

A missing component is not waivable by the approver. Where a vendor cannot supply
one, the gap is a standing control exception under EXC-PROC section 5, bounded at
90 days, and the vendor operates at reduced scope until it closes.

## 4. Approval and expiry

Review approval is recorded against the named approver and carries an explicit
expiry date. There is no grace period at expiry: production access granted to
vendor personnel lapses automatically when the vendor's review expires, under
section 3 of ACC-POL.

Approval of a vendor review is not approval of a change. A vendor whose review is
current still submits changes through the CAB on the same terms as an internal
team, and vendor personnel implementing a change are bound by CHG-STD in full.

## 5. Findings

Findings are rated critical, high, moderate, or low. Critical and high findings
block approval until remediated or accepted by the sponsoring director in writing.
Moderate and low findings are tracked to a remediation date agreed at review.

An unremediated high finding past its agreed date suspends the vendor's production
access until it closes.

## 6. Records

Vendor review records, findings, and remediation evidence are retained for six
years from the end of the vendor relationship under RET-SCH — not from the review
date, which means an active long-running vendor's earliest records are held
throughout.
