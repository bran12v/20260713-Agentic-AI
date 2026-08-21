# Release Freeze Calendar

**Doc id:** FRZ-CAL
**Doc type:** calendar
**Owner:** Delivery Engineering Council
**Effective:** 2026-01-01
**Period covered:** calendar year 2026

## 1. What a freeze is

During a declared freeze window, no production change may be implemented, whatever
its classification and whatever approval it already holds. CAB approval and
standard-change pre-authorisation are both suspended for the duration of the
window.

Two things are permitted during a freeze:

- **Emergency changes** authorised by the Duty Change Authority under section 3 of
  EXC-PROC. The emergency authorisation covers the freeze; a separate freeze
  exception is not required.
- **Changes holding a freeze exception** granted by the full CAB under section 4 of
  EXC-PROC.

## 2. The declared windows

This is the complete list of freeze windows for 2026. A window not listed here
does not exist, and no team may declare a local freeze that binds another team.

| Window | Starts | Ends | Reason |
|---|---|---|---|
| Year-end close | 2026-12-18 09:00 UTC | 2027-01-05 09:00 UTC | Client financial year-end |
| Quarter-end Q1 | 2026-03-28 17:00 UTC | 2026-04-02 09:00 UTC | Quarterly client reporting |
| Quarter-end Q2 | 2026-06-27 17:00 UTC | 2026-07-02 09:00 UTC | Quarterly client reporting |
| Quarter-end Q3 | 2026-09-26 17:00 UTC | 2026-10-02 09:00 UTC | Quarterly client reporting |
| Regulatory filing | 2026-05-11 09:00 UTC | 2026-05-16 09:00 UTC | Client regulatory submission |
| Platform migration | 2026-08-08 09:00 UTC | 2026-08-15 09:00 UTC | Data centre migration |

All times are UTC. A window that begins at 09:00 UTC begins then regardless of the
implementing team's local time; teams operating outside UTC are responsible for
converting and have on several occasions failed to.

## 3. Standing weekly constraint

Outside the windows above, production changes are not implemented after 15:00 UTC
on a Friday or at any time on a Saturday or Sunday. This is a constraint on
implementation windows under section 5 of CHG-STD, not a freeze — no exception is
required, but the change must be scheduled into a permitted window.

Emergency changes are unaffected by the weekly constraint.

## 4. Adding a window

A new window is declared by the Council with a minimum of 30 days' notice, and
this document is revised. A revision supersedes the previous version, which is
retained for seven years under RET-SCH.

Notice shorter than 30 days requires the sponsoring director's approval and is
itself recorded as an exception.

## 5. Changes in flight when a window opens

A change already implementing when a window opens completes; it is not abandoned
mid-flight. A change approved but not started does not begin. Where completion
would extend more than two hours into the window, the implementing engineer backs
out under RBK-STD rather than continuing.
