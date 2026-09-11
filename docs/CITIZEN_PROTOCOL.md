# Citizen Protocol

This document defines the public-facing Toledo flow. It should remain understandable even when the back-end framework is complex.

## Step 0 — Start with your real problem

The citizen begins in ordinary language.

Examples:

- "My orchard trees are getting worse in one low area."
- "My mother keeps missing a step in this process."
- "This machine fails only on humid days."
- "I have a recurring household problem and don't know which part to investigate first."

No research vocabulary is required.

## Step 1 — Preserve the citizen's words

The system stores:

```text
P_C = citizen_problem_verbatim
```

AI may structure it, but the original must remain visible.

## Step 2 — Separate what was observed from what is believed

AI asks for the minimum details needed to distinguish:

```text
Observation
Interpretation
Hypothesis
Prior action
Context
Unknown
```

The system does not silently turn "I think it is X" into "It is X."

## Step 3 — Form provisional K*_0

AI helps convert experiential capital into a structured candidate:

```text
citizen experience
+
AI-mediated structuring
+
accessible evidence
→
K*_0
```

`K*_0` is a knowledge-like candidate, not certified truth.

## Step 4 — Ask the cheapest safe next question

Before calling an institution, the platform asks:

```text
What is the lowest-cost action
that can materially improve the next decision
without exposing the citizen to unacceptable risk?
```

Possible answers:

- observe one more variable;
- compare affected vs unaffected cases;
- look up an existing standard practice;
- measure something inexpensive;
- ask an expert;
- send a sample to a lab;
- contact a regulator;
- stop self-experimentation and escalate immediately.

## Step 5 — Escalate only when necessary

External capability is called when the case needs:

- professional authority;
- specialized measurement;
- material safety review;
- regulatory permission;
- a qualified expert;
- laboratory or prototype infrastructure;
- a capability the citizen+AI route cannot safely provide.

The router chooses by **capability fit + accessibility + time fit + decision gain**, not prestige.

## Step 6 — Use a Case Passport

When another actor enters, the platform carries a Case Passport rather than asking the citizen to restart.

The passport records:

- original problem and goal;
- AI-structured problem;
- evidence and unknowns;
- current decision;
- requested capability;
- consent and data-use scope;
- rights/provenance state;
- deadline;
- expected return;
- fallback route.

## Step 7 — Validate the handoff

A valid handoff must preserve:

```text
meaning
requested capability
decision ownership
consent
data-use scope
return obligation
time fit
fallback
```

A phone number or generic referral is not enough.

## Step 8 — Require a Return Object

The external actor returns:

- result in usable language;
- technical result when needed;
- what is known;
- what remains unknown;
- limitations;
- the next recommended action;
- unsafe actions to avoid;
- returned data;
- follow-up trigger.

The citizen must be able to correct a misunderstanding.

## Step 9 — Act in the world

The citizen or legally appropriate decision owner takes the next action.

The result returns into the case record.

## Step 10 — Decide whether to stop

Valid outcomes include:

```text
problem resolved
existing practice correctly adopted
local fix
repeatable practice
public knowledge
research candidate
innovation candidate
```

Stopping after a good local solution is success.

## Optional innovation path

Only when warranted:

```text
local result
→ novelty / existing-solution check
→ transferability
→ innovation candidate
→ prototype / validation
→ knowledge asset map
→ utilization route
```

Possible utilization routes include:

```text
new startup
spin-off
joint venture
license
assignment / sale
technology transfer
existing-firm adoption
cooperative / community enterprise
social enterprise
contract manufacturing + brand
open / public-interest dissemination
```

The citizen does not have to become an entrepreneur.

## Citizen rights in the protocol

At minimum, a citizen should be able to:

- see the original problem statement;
- correct AI or institutional reframing;
- know who currently has the case;
- know why another institution is needed;
- know the expected cost/time where available;
- control consent and data-use scope;
- distinguish experience provenance from legal IP ownership;
- receive the result back;
- leave the process;
- challenge or reroute a failed handoff.

## What the platform must never optimize away

```text
Safety
Meaning
Rights
Consent
Decision ownership
Return to citizen
```

These are not UI details. They are architectural constraints.
