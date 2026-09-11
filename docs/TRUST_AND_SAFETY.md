# Trust and Safety Model

Toledo Citizen Platform is designed to lower the cost of disciplined problem-solving without lowering the safety threshold for consequential action.

## 1. Core principle

```text
AI-first != AI-only
```

AI may reduce the cost of articulation, structuring, retrieval, comparison, questioning, and routing. It MUST NOT silently replace professional authority, laboratory measurement, regulatory authorization, physical inspection, or independent validation when those are materially required.

## 2. Hard gates before optimization

Hard gates are evaluated before route scoring.

Typical hard gates include:

```text
material health/safety risk
licensed professional required
highly irreversible intervention
significant third-party exposure
specialized measurement is decision-critical
regulatory authorization required
consent/data-transfer constraint
rights/IP constraint
```

Hard gate states should remain typed:

```text
PASS
HOLD_UNKNOWN
FAIL
N/A
```

A favorable cost, convenience, or accessibility score MUST NOT average away `FAIL` or `HOLD_UNKNOWN`.

## 3. Action-specific readiness

The platform should ask:

```text
Is the evidence sufficient for this specific next action?
```

not:

```text
Is the whole problem solved with certainty?
```

A citizen may be ready for a reversible low-risk observation or test while not being ready for an irreversible intervention.

## 4. Escalation triggers

Escalate when one or more of the following materially apply:

- risk to life, health, safety, or major property;
- legal/professional authority is required;
- the action is difficult to reverse;
- the uncertainty directly changes a high-consequence decision;
- a measurement cannot be reliably obtained without specialist infrastructure;
- regulated products/activities are involved;
- third parties or vulnerable populations are exposed;
- the case contains unresolved rights or consent constraints.

## 5. High-stakes domains

Production deployments SHOULD define stricter jurisdiction-specific policies for at least:

```text
health / medical
legal
financial
physical safety
food / drug / regulated products
child / vulnerable-person contexts
critical infrastructure
high-value irreversible property decisions
```

The global repository defines the architecture, not country-specific professional advice rules.

## 6. AI uncertainty and disagreement

AI-generated hypotheses are proposals, not findings.

When model outputs disagree:

```text
disagreement
→ expose uncertainty
→ seek discriminating evidence
→ escalate when consequence requires it
```

Do not hide disagreement through synthetic consensus.

## 7. Meaning safety

Meaning drift is a safety issue when it changes the decision.

The platform preserves:

```text
P_C = citizen problem
P_S = AI-structured problem
P_D = disciplinary problem
```

Material reframing should be visible and correctable by the citizen before costly or irreversible action.

## 8. Institutional safety

An institution can be relevant but still non-executable.

Separate:

```text
AcademicFit
UniversityExecutability
Eligibility
ResponseTimeFit
Authority
```

A technically ideal institution that cannot respond inside the citizen's decision window is not a safe executable route unless an interim safe action exists.

## 9. Handoff safety

A route to an external actor is incomplete until the handoff carries:

```text
meaning
requested capability
decision owner
consent scope
data-use scope
return obligation
time fit
fallback
```

A generic referral should not be mistaken for a governed handoff.

## 10. Return safety

External work MUST return enough information to support the next decision:

```text
what is known
what is unknown
limitations
recommended next action
unsafe actions to avoid
returned data/result
rights/consent state
follow-up trigger
```

Institutional completion is not citizen safety if the result never returns in usable form.

## 11. Privacy and sensitive data

This public repository is not a citizen case store.

Production systems should implement:

- data minimization;
- explicit consent scopes;
- role-based access;
- encryption in transit and at rest;
- retention/deletion controls;
- audit logs;
- secret management;
- jurisdiction-specific privacy requirements;
- safe export/redaction of Case Passport views.

See [`../SECURITY.md`](../SECURITY.md).

## 12. Model/tool logging

Prompts, model outputs, tool traces, and retrieval context may contain sensitive case information and should be governed as case data in production.

Do not assume technical logs are harmless metadata.

## 13. Institution-data safety

Stale program information can create unsafe or costly routing.

For high-consequence use, verify:

```text
eligibility
current availability
legal authority
accreditation when relevant
application window
response time
```

before presenting a route as currently executable.

## 14. World-side interruption

A theory, AI answer, or expert opinion should encounter real-world constraint before stronger claims are promoted.

Examples include:

```text
measurement
controlled comparison
field test
independent review
user adoption
regulatory decision
actual transaction
```

depending on the claim.

## 15. Failure is preserved

Failed routes and failed tests are valuable evidence.

Do not erase:

```text
institution rejected case
lab unavailable
hypothesis contradicted
pilot failed
return not received
rights conflict discovered
```

Failure should update the case state and fallback logic.

## 16. Stop conditions

The platform should stop or hold when:

- a mandatory gate fails;
- critical uncertainty remains unresolved;
- the citizen withdraws consent;
- no safe executable route exists;
- action would exceed legitimate authority;
- expected harm outweighs justified learning/action value.

`HOLD_UNKNOWN` is preferable to invented certainty.

## 17. Safety invariant

The product must never optimize away:

```text
Safety
Meaning
Rights
Consent
Decision ownership
Return to citizen
```

These are architectural constraints, not optional UX preferences.
