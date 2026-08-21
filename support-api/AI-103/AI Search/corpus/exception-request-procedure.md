# Exception Request Procedure

**Doc id:** EXC-PROC
**Doc type:** procedure
**Owner:** Delivery Engineering Council
**Effective:** 2026-03-01

## 1. Scope

This procedure covers three exception types:

- **Emergency change authorisation** — proceeding with a production change before
  CAB approval, under section 4.2 of CHG-STD.
- **Freeze exception** — implementing during a declared freeze window under
  FRZ-CAL.
- **Standing control exception** — operating outside a control for a bounded
  period.

Each type has a different authority, a different evidence requirement, and a
different expiry. They are not interchangeable, and an approval of one does not
imply the other.

## 2. The Duty Change Authority

The Duty Change Authority is a named individual on the CAB roster, on call in
weekly shifts, empowered to authorise emergency changes between board sessions.
The roster is published alongside the on-call rota (ONC-RUN).

The Duty Change Authority may authorise an emergency change. They may **not**
grant a freeze exception, add an entry to the Standard Change Catalog, or approve
a normal change. Those remain board decisions.

## 3. Emergency change authorisation

### 3.1 Grounds

An emergency change is justified only where the change restores service during an
active Severity 1 or Severity 2 incident, or closes a security exposure being
actively exploited. Severity definitions are in SEV-MTX.

Anticipated urgency is not an emergency. A change that is merely late, or whose
window was missed, follows the normal route.

### 3.2 Authorisation

The implementing engineer contacts the Duty Change Authority, who authorises or
declines verbally and records the decision in the change record within the hour.
Verbal authorisation is sufficient to begin implementation.

### 3.3 Retrospective review

**An emergency change must complete retrospective review within 24 hours of
implementation.** The review is conducted by the CAB or, out of session, by two
board members who were not involved in the change.

The review establishes four things: that the grounds in 3.1 were met, that the
backout path was verified, that the blast radius matched what was represented, and
whether the change type should be added to the Standard Change Catalog.

The 24-hour clock runs from the completion of implementation, not from
authorisation and not from incident closure. A change implemented across a weekend
is reviewed on the same clock; the roster exists so there is always a quorum
available.

### 3.4 Failure to review

Where retrospective review has not completed within 24 hours, the change is
recorded as a control failure against the implementing team under section 4.2 of
CHG-STD, and that team's standard-change pre-authorisation is suspended until the
review closes. Suspension means every change from that team, including catalog
entries, routes through full CAB review.

## 4. Freeze exception

A freeze exception is granted only by the full CAB, in session, and requires the
sponsoring director's written support. The Duty Change Authority cannot grant one.
An emergency change during a freeze does not require a separate freeze exception —
the emergency authorisation covers it — but the retrospective review in 3.3 must
address the freeze impact explicitly.

## 5. Standing control exception

A standing exception is bounded at 90 days and may be renewed once. A second
renewal requires the control owner to either amend the control or accept the risk
formally. Standing exceptions are reviewed monthly by the Council and expire
automatically; there is no grace period.
