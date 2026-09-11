# Glossary and Controlled Vocabulary

This glossary is the primary terminology reference for Toledo Citizen Platform. Product UI may use simpler language, but implementation, schemas, routing, and governance should map back to these terms.

## Citizen and knowledge terms

### Citizen
The person or community actor who owns the original real-life problem or goal. A citizen does not need to be a researcher, founder, or subject-matter expert.

### Experiential Capital (`E_c`)
Decision-relevant experience, observation, context, practice, prior success/failure, constraints, and goals held by the citizen before formal institutional processing.

### AI-Mediated Exchange
AI-assisted clarification, structuring, retrieval, comparison, questioning, hypothesis generation, and routing. AI mediation does **not** itself provide professional authority, independent validation, or truth certification.

### Knowledge-like Capital / `K*_0`
A provisional structured candidate produced from citizen experience, AI-mediated exchange, and accessible evidence. It is useful for inquiry and routing but is not automatically verified knowledge.

### Escalated Knowledge-like Candidate / `K*_I`
A knowledge-like candidate strengthened by expert, laboratory, university, professional, regulatory, or other institutional contribution when the case requires it.

## Problem representations

### `P_C` — Citizen Problem
The citizen's own problem statement, preserved verbatim or as close to verbatim as practical. It MUST NOT be overwritten by later technical reframing.

### `P_S` — Structured Problem
The AI-mediated structured version of the citizen problem used to organize observations, unknowns, hypotheses, constraints, and next actions.

### `P_D` — Disciplinary Problem
A specialist or institutional formulation used for research, technical service, regulation, or professional work. It MUST remain traceable to `P_C` and `P_S`.

### Problem Signature
A domain-neutral operational readout used for routing. It may contain intent, object readout, observed difference, evidence need, stakes, authority need, candidate alternatives and next discriminating action. It is **not** a diagnosis and does not replace `P_C`.

### Candidate Signature
One possible AI/human/evidence-supported translation of the case. Multiple candidates may remain live. A candidate is not promoted merely because an AI generated it.

### Endorsed Signature
A working Problem Signature explicitly selected through recorded citizen endorsement, evidence support, or the governed process appropriate to the case. Endorsement does not make it truth.

### Problem Facet Provenance
The recorded source of a material signature facet, such as citizen wording, citizen clarification, AI inference, world measurement, original document, expert return, or institutional return.

### Context Gap
A material event-specific condition that is not currently observed or recorded. A Context Gap MUST remain unknown rather than being silently converted into an AI-inferred fact.

### Barrier Signature
A separate description of what blocks progress. The reference barrier dimensions are knowledge, skill, language, tool, resource/time, network, credential, permission, opportunity, and unknown.

### Practice Context
Occupation, repeated practice, local setting, tacit distinctions, role, tools, and other situated information that may carry experiential expertise. Practice Context is relevant evidence/context but does not automatically select a bespoke core protocol.

### Protocol Primitive
An operational verb available to the compiler, such as observe, compare, measure, test, decide, repair, validate, hold, or scale. A Protocol Primitive is not asserted to be a fundamental metaphysical kind of problem.

### Domain Adapter
An optional specialization that adds domain vocabulary, hazards, professional boundaries, measurements/sample rules, regulation or provider mappings without redefining global Case Passport, Decision Thread, provenance, hard-gate, Return Gate, or equation semantics.

## Case continuity and multi-decision terms

### Case Passport
A versioned object that carries the same case across citizens, AI systems, experts, universities, public agencies, laboratories, regulators, and other actors without forcing a restart. A Case Passport may contain one or more Decision Threads.

### Decision Thread
One decision-specific routing subgraph inside the same Case Passport. A Decision Thread carries its own decision, P0-P11 phase, evidence/unknowns, risk, requested capability, dependencies, external-actor state, Return Gate state and outcome state when needed.

A Decision Thread is **not** a new case, a new maturity scale, or a new Toledo equation.

### Primary Thread
The Decision Thread selected as the backward-compatible projection surface for legacy fields:

```text
current_phase    = primary_thread.phase
current_decision = primary_thread.decision
```

`Primary Thread` means compatibility/reference focus, not "the truest" or universally most important decision.

### Thread Dependency
A declared relation indicating that one Decision Thread should not execute its downstream action until another Decision Thread is closed or cancelled.

### Blocking Thread
An unresolved dependency listed in `blocking_threads`. A blocking thread prevents ordinary downstream execution but does not mean the case failed.

### Dependency Hold
The runtime state used when a Decision Thread has unresolved dependencies:

```text
next_action = HOLD
status = HOLD_FOR_DEPENDENCY
```

Hard safety/authority escalation outranks an ordinary Dependency Hold.

### Required Thread
A Decision Thread whose `required_for_case_closure` is true. A multi-decision case cannot close while a required, non-cancelled thread remains unresolved.

### Thread Closure
The closure of one decision-specific subgraph. Local threads may close without a fake institutional Return Object when no external actor was used and safety/authority is clear. External threads require a passing Return Gate. Thread Closure does not automatically imply Case Closure.

### Civic Knowledge Case Steward
A coordination role responsible for continuity, routing, consent scope, return obligations, dependency visibility and fallback activation. A steward is not automatically an expert, regulator, or decision authority.

### Capability Request
A structured request that identifies the exact capability needed, the decision it should unlock, the minimum required output, current evidence, uncertainty to reduce, timing, cost constraints, and return format.

### Referral
A pointer to another actor or institution. A referral does not imply continuity or return.

### Handoff
A transfer of case/thread context plus requested capability, consent/data scope, decision owner, response-time requirement, return obligation, and fallback route.

### Collaboration
Two or more actors remain jointly active around the same persistent case/thread state.

### Return Object
The structured result returned by an external actor: plain-language result, technical result where needed, knowns, unknowns, limitations, next action, unsafe actions to avoid, returned data, rights state, and follow-up trigger.

### Return Gate
The gate that prevents external institutional/professional work from being treated as complete until a usable result reaches the citizen or correct decision owner. A citizen+AI/world-only local thread with no external actor may use `NOT_APPLICABLE` rather than manufacturing a fake Return Object.

### External Actor Used
A case/thread state indicating that an expert, institution, provider, regulator, laboratory or equivalent external actor actually entered the execution route. When true at thread level, thread closure requires a passing Return Gate.

## Routing terms

### Capability
A concrete service or authority needed by the case, such as expert consultation, field inspection, laboratory measurement, sample analysis, process audit, prototype support, regulatory classification, legal authorization, standards testing, incubation, funding, or market matching.

### Route
A sequence of capabilities and actors selected to unlock the next justified decision.

### Minimum-Sufficient Route
The lowest-burden route that still satisfies safety, evidence, authority, rights, dependencies, and decision-usability requirements.

### Hard Gate
A typed requirement that cannot be averaged away by a soft score. Typical states are `PASS`, `HOLD_UNKNOWN`, `FAIL`, and `N/A`. Hard safety/authority gates also take precedence over ordinary Decision Thread dependency holds.

### Soft Score
A comparative heuristic used only after hard gates are satisfied, for example cost, access burden, timeliness, or expected decision gain.

### Phase (`P0`–`P11`)
A routing coordinate describing the current decision need. Phases are **not** a maturity ranking and are not mandatory linear stages. In multi-decision cases, different Decision Threads may legitimately occupy different phases at the same time.

## Institutional terms

### Institution Capability Record
A machine-readable description of a specific mechanism/service, not merely an institution name. It includes phase fit, target users, eligibility, access, capability, geography, provenance, and freshness.

### Institution Class (`I0`–`I9`)
A high-level routing category such as citizen-facing service, technical infrastructure, innovation support, IP/knowledge utilization, regulator/standards body, growth/finance, global/export, or policy orchestration.

### Accessibility Class (`A0`–`A4`)
A description of practical public entry burden. Accessibility is not a quality ranking.

### Country Adapter
A jurisdiction-specific package containing institutions, regulators, laws/policies, access routes, language/localization, and local constraints while leaving jurisdiction-neutral core logic unchanged.

### System/Policy Body
An actor whose primary role is ecosystem design, policy, or orchestration rather than direct citizen case handling.

## Knowledge-utilization terms

### Knowledge Asset Map (`K_MAP`)
A decomposition of the relevant knowledge bundle into claims, know-how, processes, data, artifacts, rights, relationships, context, trust/brand, and market knowledge.

### Knowledge Utilization Route
The execution path selected for useful knowledge, including local use, public dissemination, license, assignment, technology transfer, existing-firm adoption, startup, spin-off, joint venture, cooperative/community enterprise, social enterprise, or another structure.

### Commercialization Vehicle
The organizational/transaction form used to capture or deliver value. It is distinct from a matching channel such as an IP marketplace.

### Business-0 Formed (`B0_F`)
A minimal accountable venture state capable of attempting a real transaction.

### First Economic Cycle Closed (`B0_C`)
A formed venture that has completed an independently grounded first economic loop with delivery, value exchange, true cost recording, and learning.

## Governance and rights terms

### Experience Provenance
Traceability of who originated an observation or situated contribution and in what context. Provenance is not automatically legal IP ownership.

### Decision Owner
The actor with legitimate authority to make the next material decision. Advice does not automatically transfer decision authority. Different Decision Threads may have different decision owners when legitimately required.

### Meaning Preservation
The requirement that citizen goals, material constraints, risk tolerance, and unresolved uncertainty remain represented across reframing, thread decomposition and handoff.

### Epistemic Capture
A failure mode where a more powerful actor's framing replaces the citizen's actual problem or makes correction impractical.

### Rights Decomposition
Separate tracking of data rights, inventorship, authorship, IP ownership, publication rights, commercial rights, confidentiality, and benefit sharing.

## Government function terms

Government is not one undifferentiated actor. Toledo distinguishes:

- `G_service` — advice, testing, extension, technical service;
- `G_funder` — grants, co-funding, financial support;
- `G_regulator` — authorization, classification, enforcement;
- `G_standard` — standards and conformity infrastructure;
- `G_procurement` — government as buyer/adopter;
- `G_policy` — ecosystem and policy design.

## Core non-collapse statements

```text
AI-first != AI-only
Observation != Interpretation != Diagnosis
Occupation != ProtocolSelector
Industry != ProtocolSelector
PracticeContext != IrrelevantContext
P_C != ProblemSignature
ProblemSignature != Diagnosis
CandidateSignature != EndorsedSignature
AITranslation != CitizenObservation
Unknown != Failure
MissingEvidence != NegativeEvidence
DomainAdapter != NewCore
ProviderName != Capability
Case != SingleDecision
DecisionThread != NewCase
PrimaryThread != MostImportantTruth
ThreadPhase != CaseMaturity
BlockedThread != FailedCase
ThreadClosure != CaseClosure
Academic capability != university executability
Referral != Handoff != Collaboration
Institutional output != Citizen outcome
Grant approval != Regulatory approval
Experience provenance != IP ownership
Company registration != Business-0
Innovation success != Creator becomes entrepreneur
Vehicle != Matching channel
Works here != Transfers elsewhere
```
