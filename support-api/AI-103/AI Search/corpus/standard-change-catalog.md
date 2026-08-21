# Standard Change Catalog

**Doc id:** CHG-CAT
**Doc type:** catalog
**Owner:** Change Advisory Board
**Effective:** 2026-03-01
**Review cadence:** quarterly

## 1. Status of this catalog

This catalog is the complete and closed list of change types the Change Advisory
Board has pre-authorised. A change type that does not appear below is **not** a
standard change, however routine it may appear in practice.

Pre-authorisation is granted under section 4.1 of the Production Change Management
Standard (CHG-STD). This catalog does not restate the approval rule; it enumerates
the exceptions to it.

## 2. Conditions attaching to every entry

An entry confers pre-authorisation only where all of the following hold. If any
condition fails, the change reverts to normal classification and requires CAB
approval.

1. The change matches the catalog entry in scope, target class, and backout path.
2. The implementation falls inside an approved window and outside a declared
   freeze.
3. The verified backout path required by RBK-STD is recorded on the change.
4. The implementer holds current production access under ACC-POL.

## 3. Catalog entries

### SC-01 — TLS certificate rotation

Replacement of a TLS certificate on a load balancer, ingress controller, or
service endpoint with a certificate issued by an approved internal or public
certificate authority, where the subject, subject alternative names, and key
algorithm are unchanged.

**Not covered:** a rotation that changes the issuing authority, adds or removes a
subject alternative name, or moves the certificate to a different key algorithm.
Those are normal changes.

### SC-02 — Horizontal scaling within approved bounds

Increasing or decreasing replica count for an existing workload within the minimum
and maximum recorded on the workload's capacity plan.

**Not covered:** changing the recorded bounds themselves.

### SC-03 — Log verbosity adjustment

Changing the log level of a running service to any level at or above `INFO`.

**Not covered:** enabling `DEBUG` or `TRACE` in production, which may emit client
data and is a normal change requiring a data-handling review.

### SC-04 — Additive database index creation

Creating a non-unique index on an existing table using an online, non-blocking
index build.

**Not covered:** any index that enforces uniqueness, any change to an existing
index, and any blocking build. Database schema changes generally are normal
changes; this entry is the single narrow exception.

### SC-05 — Feature flag toggle for an already-released capability

Enabling or disabling a feature flag whose underlying capability has already
passed a normal change and is deployed to production.

**Not covered:** the first activation of a flag for a capability that has not been
through a normal change.

### SC-06 — Routine dependency patch at patch version

Applying a patch-version dependency upgrade with no interface change, where the
service's automated test suite passes and the upgrade carries no advisory above
moderate severity.

**Not covered:** minor or major version upgrades, and any upgrade responding to a
high or critical advisory — the latter follows the emergency route under
EXC-PROC.

### SC-07 — Scheduled credential rotation for a service principal

Rotating the secret or certificate of a service principal on its documented
rotation schedule, where the principal's role assignments are unchanged.

**Not covered:** any rotation that alters role assignments or scope.

### SC-08 — DNS record time-to-live adjustment

Changing the TTL of an existing DNS record without altering its value or type.

**Not covered:** creating, deleting, or repointing a record.

## 4. Additions to this catalog

A team may propose a new entry through the CAB. A proposal must include the change
type's blast radius, its verified backout path, and evidence of at least ten
consecutive incident-free normal changes of that type. Approval of an entry is
itself a CAB decision recorded in the minutes.
