# Toledo Flexible Execution Routing v0.1

Status: **normative additive runtime contract / pre-alpha**.

This layer extends the existing Toledo Citizen Platform without replacing the Case Passport, Problem & Capability Grammar, Decision Threads, P0-P11 routing coordinates, hard gates, institution registry, Return Gate, or upstream equation bindings.

Its purpose is to answer a narrower execution question:

```text
Given the current decision state,
what kind of knowledge, human expertise, world contact, tool,
infrastructure, or authority is actually needed next?
```

It does **not** turn P0-P11 into a mandatory sequence and does not require an expert merely because a thread is at a particular phase.

## 1. Anchor-preserving relationship

The existing path remains authoritative:

```text
P_C
-> Candidate Signature(s)
-> Endorsed / unresolved working signature
-> Barrier State
-> Decision Thread
-> Minimal Protocol
-> Capability Need
-> Provider / World Action
-> Return / Case Event
```

This document adds one execution translation layer:

```text
Capability Need
+ Evidence Need
+ Barrier State
+ Risk / Authority State
+ Context Gap
+ Decision Thread dependencies
+ Phase as routing context
        ↓
Execution Requirement(s)
        ↓
AI-mediated connection to
knowledge-like material / human experts / tools / infrastructure / authority / world test
```

The new layer is additive:

```text
Phase != ExpertSelector
Phase != MandatorySequence
ProviderName != Capability
Capability != ExecutionActor
```

## 2. AI role: mediator and translator

AI is the connective layer, not a third expert category.

```text
Citizen / World
    ↕
AI mediator / translator
    ↕
knowledge-like sources and readouts
interaction experts
field/front-line experts
tools and measurement
institutions and authorities
    ↕
World return
```

AI may:

- translate citizen language into a capability request;
- translate expert or institutional language back into usable citizen language;
- connect evidence, experts, tools, and institutions;
- compare routes;
- expose missing context;
- propose a bounded world test;
- preserve provenance across translations.

AI does not thereby become:

```text
a licensed professional
a front-line expert
a regulator
a laboratory
an independent validator
a truth certificate
```

Multiple AI outputs with shared ancestry do not automatically create independent validation.

## 3. Three distinct knowledge/expertise objects

Toledo MUST NOT collapse the following into one generic `expert` object.

### 3.1 Knowledge-like material

Examples:

```text
structured AI readout
prior case
manual
standard
paper
dataset
original record
retrieved public information
provisional synthesis
```

This may contribute to `K*_0` or, after external contribution, an escalated `K*_I` readout.

```text
KnowledgeLike != HumanExpert
KnowledgeLike != Truth
KnowledgeLike != Authority
```

It may be useful enough to support action while still remaining provisional, provenance-bound, and corrigible.

### 3.2 Interaction Expert

An `INTERACTION_EXPERT` contributes expertise primarily through interaction such as:

```text
elicitation
interpretation
questioning
teaching
comparison
negotiation
stakeholder alignment
requirements clarification
decision support
```

This role is especially useful when meaning, goals, trade-offs, tacit distinctions expressed in conversation, institutional language, or stakeholder interpretation matter.

An Interaction Expert may operate remotely and need not have direct physical contact with the system under study.

### 3.3 Field / Front-line Expert

A `FIELD_EXPERT` contributes situated expertise grounded in direct repeated contact with the world, for example:

```text
operator
technician
farmer
nurse
mechanic
production worker
installer
field officer
local practitioner
```

Its distinctive value may include:

```text
tacit distinctions
sensory cues
workarounds
failure patterns
local constraints
physical access
repeated world feedback
```

```text
FieldExpert != InteractionExpert
```

One person may satisfy both roles, but the routing reason should remain explicit.

## 4. Authority and infrastructure are overlays

Some execution requirements are not adequately represented as ordinary expert roles.

Reference overlays include:

```text
LICENSED_PROFESSIONAL
LAB_INFRASTRUCTURE
REGULATORY_AUTHORITY
MEASUREMENT_TOOL
ORIGINAL_DOCUMENT
AUTHORITY_OR_PERMISSION_PATH
```

For example, a field expert may understand a machine extremely well while lacking the legal authority required to certify it. A regulator may possess authority without being the best actor for process diagnosis.

```text
Expertise != LegalAuthority
Advice != AccreditedMeasurement
AccreditedMeasurement != RegulatoryAuthorization
```

## 5. Non-linear execution rule

P0-P11 remain routing coordinates, not a conveyor belt.

A case may legitimately:

```text
observe
-> act locally
-> test in the world
-> reach a bounded market
-> return to measurement or expert review later
```

when the action is sufficiently bounded and reversible and no hard safety, authority, permission, credential, unresolved-return, or dependency gate blocks it.

Therefore:

```text
EarlierPhase != MustWaitForAllLaterExpertise
LaterMarketContact != ProofOfValidity
MarketEntry != CaseClosure
```

A real transaction or market test can itself generate world-side evidence.

## 6. Bounded forward experiment

A compiler may expose:

```text
forward_experiment.allowed = true
```

when, at minimum:

```text
no hard escalation is active
no required licensed/lab/regulatory authority is unresolved
no explicit permission/credential barrier blocks action
no Decision Thread dependency blocks the decision
Return Gate is not FAIL/HOLD_UNKNOWN
irreversibility is not known HIGH
third-party exposure is not known HIGH
```

When a market signal is present, the compiler may additionally expose:

```text
BOUNDED_MARKET_TEST
```

as a candidate world-side information route.

This is not permission to ignore law, safety, consent, rights, consumer protection, professional boundaries, or sector regulation.

It is a rule against unnecessary sequencing.

## 7. Execution Requirement Matrix

The matrix consumes multiple coordinates rather than phase alone.

Reference inputs:

```text
phase
problem signature
evidence need
barrier state
unknown/context gap
requested capability
risk state
authority need
irreversibility
third-party exposure
dependency state
return-gate state
jurisdiction/domain constraints
```

Reference execution classes include:

```text
KNOWLEDGE_LIKE_SOURCE
INTERACTION_EXPERT
FIELD_EXPERT
MEASUREMENT_TOOL
ORIGINAL_DOCUMENT
LAB_INFRASTRUCTURE
LICENSED_PROFESSIONAL
REGULATORY_AUTHORITY
AUTHORITY_OR_PERMISSION_PATH
WORLD_TEST
BOUNDED_MARKET_TEST
HARD_GATE_EXTERNAL_ROUTE
```

The list is an implementation vocabulary and may evolve without claiming a universal ontology of action.

Each requirement carries:

```text
class
requiredness = REQUIRED | CANDIDATE | OPTIONAL
reasons[]
basis[]
```

`CANDIDATE` means the route is useful to consider, not mandatory.

## 8. Phase use

Phase is allowed to contribute prior routing context, but it must not dominate the matrix.

Examples:

```text
P0-P1 often increase the value of observation, evidence and measurement
P3 often increases the probability of external expert/institution use
P4-P6 often increase the value of knowledge-like sources, research, validation or rights evidence
P7-P11 often increase the value of partner, market, transaction, scale or cross-border world tests
```

But these are not hard mappings.

A P1 thread can reach a bounded customer test if safe and useful. A P10 thread can still need a basic field observation. A P3 thread may be resolved locally if the supposed need for escalation disappears after better evidence.

## 9. Expert selection

When the working signature says `authority_need = EXPERT`, the compiler must still determine which expert relation is relevant.

Reference logic:

```text
situated / physical / operational context dominant
-> FIELD_EXPERT

meaning / interpretation / stakeholder / decision interaction dominant
-> INTERACTION_EXPERT

mode unresolved
-> keep both as candidates / HOLD_UNKNOWN as needed
```

The system should not route to a prestigious institution merely because it contains experts.

## 10. Capability-to-provider matching

The execution matrix stops at the type of execution needed.

Country/domain adapters and the Institution Capability Registry then answer:

```text
Which currently executable provider can supply that capability
under the relevant jurisdiction, access, eligibility, time, cost,
accreditation and authority constraints?
```

This preserves:

```text
ExecutionRequirement != Provider
Capability != InstitutionName
```

## 11. World return

The purpose of expert/tool/institution routing is to improve the next decision, not to create institutional activity for its own sake.

Every external route remains subject to the existing Return Gate.

A world/market experiment returns through ordinary Case Events when no external institutional actor was used.

## 12. Examples

### Intermittent machine problem

```text
P_C:
"The machine starts some mornings but not others."

unknown cause
physical system
low known irreversibility
no authority gate

candidate requirements:
KNOWLEDGE_LIKE_SOURCE
FIELD_EXPERT
MEASUREMENT_TOOL
WORLD_TEST
```

AI connects the operator's observations to a test plan and, if useful, a technician or measurement tool. AI is not the technician.

### Market-first learning

```text
P_C:
"Customers like the sample but I do not know whether they will pay."

low-risk reversible offer
no regulatory/permission block

candidate route:
INTERACTION_EXPERT (optional/candidate)
BOUNDED_MARKET_TEST
WORLD_TEST
```

The bounded market test may occur before formal innovation or expert escalation. A sale is evidence of one economic interaction, not proof that every quality, legal, safety, or scale question is solved.

### Regulated claim

```text
intended public claim
regulatory authority required

required route:
REGULATORY_AUTHORITY
HARD_GATE_EXTERNAL_ROUTE
```

AI may translate the question and prepare the record, but cannot satisfy the authority gate itself.

## 13. Machine contract

Reference schema:

```text
packages/schemas/execution-routing.schema.json
```

`compile_protocol()` exposes the routing object as:

```text
execution_routing
execution_requirements
```

The object explicitly reports:

```text
phase_semantics = ROUTING_CONTEXT_NOT_MANDATORY_SEQUENCE
ai_role.class = MEDIATOR_TRANSLATOR
expert_classes = [INTERACTION_EXPERT, FIELD_EXPERT]
knowledge_like class/status
route_mode
requirements[]
forward_experiment
```

## 14. Non-collapse rules

```text
AI != ExpertClass
AITranslation != IndependentValidation
KnowledgeLike != HumanExpert
KnowledgeLike != TruthCertificate
InteractionExpert != FieldExpert
Expertise != Authority
Phase != ExpertSelector
Phase != MandatorySequence
MarketTest != ValidationOfEverything
MarketEntry != CaseClosure
ForwardExperiment != PermissionToIgnoreHardGates
Capability != Provider
```

## 15. Status boundary

This matrix is product/runtime architecture.

It is not claimed to be:

```text
a new Toledo equation
a universal ontology of expertise
a proof that all problems share one sequence
a replacement for domain judgment
a substitute for professional/regulatory authority
```

Mathematical authority remains in `morrocwi/toledo`. This layer must remain corrigible under cross-domain and real-world testing.
