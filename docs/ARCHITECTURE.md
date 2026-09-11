# Toledo Citizen Platform — Reference Architecture

## Purpose

The platform connects a citizen's real-life problem to the smallest sufficient combination of AI, evidence, expert capability, institutional infrastructure, and world-side testing needed for a safe, useful next action.

The architecture is intentionally split into two views:

```text
CITIZEN VIEW
simple, low-friction, problem-centered

BACK-END GOVERNANCE ENGINE
traceable, phase-aware, rights-aware, risk-aware, dependency-aware, institution-aware
```

The back end may be complex. The citizen should not need to understand the bureaucracy.

## System graph

```text
Citizen
  ↕
AI Exchange Layer
  ↓
Domain-Neutral Problem & Capability Grammar
  ↓
Case Passport
  ↓
Decision Thread(s)
  ↓
Risk / Evidence / Authority / Dependency Gates
  ↓
Capability Router
  ├── self-observation / public knowledge
  ├── expert
  ├── university / laboratory
  ├── public service
  ├── funder
  ├── regulator / standards body
  └── market / transfer / venture infrastructure
  ↓
Contribution / World Action
  ↓
Return Object when external work is used
  ↓
Citizen / Decision Owner
  ↓
World-side action
  ↓
Case + Thread state update
```

## Core modules

### 1. Citizen Intake

Captures the smallest useful problem object:

```text
problem_in_own_words
goal
observed_facts
prior_attempts
constraints
available_resources
perceived_risk
practice_context when useful
```

The platform should never require a citizen to formulate a research question before help begins.

### 2. AI Exchange

AI is a mediator and structuring layer. It can:

- clarify language;
- separate observation from interpretation;
- generate candidate hypotheses;
- generate multiple candidate problem signatures;
- propose candidate Decision Threads when several decisions are present;
- retrieve and compare accessible evidence;
- expose missing information and contradictions;
- propose low-cost next information actions;
- identify escalation flags;
- prepare a capability request.

AI does not silently satisfy professional, regulatory, laboratory, independent-validation, dependency, or Return Gate requirements.

### 3. Domain-Neutral Problem & Capability Grammar

The core must not grow one protocol per occupation or domain.

```text
Occupation != ProtocolSelector
Industry != ProtocolSelector
```

Instead, it preserves the citizen's original problem and carries candidate routing readouts containing intent, object readout, evidence need, alternatives, risk/authority state, context gaps and barriers.

```text
P_C
  → Candidate Signature(s)
  → Endorsed / unresolved working signature
  → Barrier State
  → Minimal Protocol
  → Capability Need
```

Occupation and practice history remain context because they may carry experiential expertise. They do not automatically select a bespoke core branch.

The grammar is an operational routing architecture, not a claim to have discovered an exhaustive ontology of human problems.

See [`PROBLEM_CAPABILITY_GRAMMAR.md`](PROBLEM_CAPABILITY_GRAMMAR.md).

### 4. Case Passport

A versioned persistent object that carries the same case across actors without forcing the citizen to restart.

It preserves:

- the citizen's verbatim problem;
- practice context without turning it into a protocol selector;
- AI-structured and disciplinary representations;
- candidate/endorsed problem signatures and provenance;
- known/unknown context and barriers;
- shared evidence, uncertainty and risk;
- consent and data-use scope;
- rights and provenance;
- Decision Threads and their dependencies;
- decision owner(s);
- response deadlines;
- return obligations;
- fallback routes.

### 5. Decision Threads

A Case Passport may contain several decision-specific subgraphs at once.

```text
Case != SingleDecision
```

Each Decision Thread carries:

```text
decision
phase
thread-local evidence / unknowns / hypotheses
risk state
requested capability
dependencies
external actor / Return Gate state
outcome state
```

The existing fields remain as a compatibility projection:

```text
current_phase    = primary_thread.phase
current_decision = primary_thread.decision
```

This preserves the original P0-P11 anchor rather than replacing it.

A thread whose dependencies are unresolved is `BLOCKED`. The compiler emits `HOLD` for that decision unless a hard safety/authority requirement demands escalation first.

```text
HardSafetyEscalation > DependencyHold
```

See [`DECISION_THREADS.md`](DECISION_THREADS.md) and ADR 0005.

### 6. Safety / Authority Gates

Hard gates are evaluated before optimization and before ordinary dependency waits.

Examples:

```text
licensed professional required
material health/safety risk
highly irreversible action
specialized measurement required
regulatory authorization required
significant third-party exposure
```

A hard gate cannot be averaged away by a favorable score elsewhere.

### 7. Minimum-Sufficient Router

The router minimizes total burden subject to safety, evidence, rights, authority, dependency, and usability constraints.

The conceptual objective is registered in the Toledo mathematics repository. This implementation repository consumes the equation contract; it does not redefine it.

### 8. Capability Registry

Institutions are indexed by capability rather than prestige, occupation, or industry label.

Example capability types:

```text
field inspection
expert consultation
laboratory measurement
sample analysis
document interpretation
process audit
prototype support
pilot plant
standards / certification
IP / TTO
business incubation
community validation
funding
regulatory authority
export / market access
```

The registry must store eligibility, location/coverage, cost/co-funding, turnaround, accreditation when relevant, current availability, and `last_verified`.

### 9. Optional Domain Adapters

The global core remains domain-neutral. A domain adapter is loaded only when specialized vocabulary, hazards, measurement/sample rules, professional boundaries, regulation, or provider mappings are materially necessary.

A domain adapter may specialize constraints but MUST NOT redefine:

```text
P_C preservation
Case Passport identity
Decision Thread semantics
P0-P11 semantics
provenance semantics
hard-gate semantics
Return Gate semantics
equation authority
```

### 10. Cross-Actor Continuity

The system separates:

```text
Referral
Handoff
Collaboration
```

A valid handoff carries meaning, requested capability, consent, decision ownership, response-time fit, return obligation, and fallback route.

### 11. Return Gate

Every external contribution returns as a structured object with:

```text
plain-language result
technical result if needed
what is known
what is unknown
limits / confidence
recommended next action
unsafe actions to avoid
returned data
rights state
follow-up trigger
```

Institutional output is not citizen outcome until it returns in usable form.

A local thread that never used an external actor does not manufacture a fake institutional Return Object merely to close. It may close only when its outcome is recorded and hard safety/authority constraints are satisfied.

For multi-decision cases, case closure additionally requires all required non-cancelled threads to be closed.

## State model

A case carries orthogonal state families:

```text
citizen_entry
problem_signature
barrier_state
decision_threads
epistemic
cross_actor_bridge
governance
field_preinnovation
innovation
knowledge_asset
utilization
business_zero
business_dynamics
regulatory
structural
conversion_control
impact
```

Do not compress the full case into one global maturity score.

## Routing phases

`P0`–`P11` remain coordinates for routing, not a mandatory linear funnel. In a complex case they are coordinates of Decision Threads, not one scalar maturity value for the entire case.

A quality thread may be at P1 while a scale thread is at P10 and a regulatory thread is at P3. A downstream thread can be blocked by the unresolved upstream decision without changing any phase definition.

A local thread may terminate at P2 as a successful resolution. A public-knowledge route may bypass venture formation. A license route may bypass founder-operated Business-0. A regulated product may activate a regulatory overlay early.

## Global / local / domain split

The platform core is jurisdiction-neutral and domain-neutral at the protocol level.

Country adapters provide:

- institutions;
- laws and regulators;
- standards;
- funding/support mechanisms;
- language/localization;
- geography/access constraints;
- culturally relevant field context.

Optional domain adapters provide specialized constraints only when needed.

Thailand is the first reference country adapter because the framework has already mapped Technology Clinics, regional science parks, universities, NSTDA/ITAP, TISTR, NIA, DIP/IP Mart, TED Fund, depa, PMUC, DIPROM, OSMEP, DBD, sector regulators, DITP, EXIM Thailand, and related mechanisms.

## Repository authority

Mathematical/equation provenance belongs in `morrocwi/toledo`.

This repository may contain:

- typed references to equation IDs;
- executable routing logic derived from those equations;
- schemas and validation code;
- problem/capability grammar and Decision Thread orchestration;
- UI and orchestration;
- domain/country adapters.

Decision Threads are an implementation architecture object. They do not silently create new mathematical authority.

The repository must not silently mutate canonical Toledo equations.
