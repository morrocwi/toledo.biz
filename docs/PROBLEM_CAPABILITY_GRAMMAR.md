# Toledo Domain-Neutral Problem & Capability Grammar

Status: **normative architecture extension / pre-alpha**.

This layer extends the existing Toledo Citizen Platform without replacing the Case Passport, Protocol Compiler, institution registry, P0–P11 routing model, or upstream equation bindings.

Its purpose is to prevent domain and occupation explosion while preserving the citizen's original problem, situated experience, uncertainty, provenance, and world-side correction.

## 1. Why this layer exists

A scalable citizen platform cannot maintain one protocol per occupation, crop, machine, profession, or life domain.

```text
Occupation -> bespoke protocol
```

would grow without bound and would silently make occupation labels carry more epistemic weight than the actual problem state.

The core instead uses a domain-neutral operational grammar:

```text
Citizen problem
    -> candidate problem signatures
    -> endorsed working signature
    -> barrier state
    -> minimum relevant protocol
    -> capability need
    -> optional domain adapter
    -> executable provider
    -> world return
```

The grammar is **not** claimed to be an exhaustive ontology of all human problems. It is an operational readout for routing and must remain revisable under cross-domain tests.

## 2. Constitutional alignment

This layer is designed to remain consistent with the Human–AI Readout programme in *Written by AI. Still True. Edition 1.2* (2026), DOI `10.5281/zenodo.22520849`.

The relevant commitments are:

```text
readout != world
source attribution requires provenance
downstream specificity must disclose augmentation
AI contribution != citizen observation
problem representation must not overwrite lived wording
unknown / unresolved is a valid state
domain semantics enter through declared translation
human/world return is required for practical closure
AI is not the sole certifier in critical cases
```

This repository treats those commitments as architectural lineage, not as independent empirical validation of this implementation.

## 3. Core non-collapse rules

```text
Occupation != ProtocolSelector
PracticeContext != IrrelevantContext
P_C != ProblemSignature
ProblemSignature != Diagnosis
CandidateSignature != EndorsedSignature
AITranslation != CitizenObservation
Classification != ObservedFact
ProtocolPrimitive != FundamentalProblemKind
ProviderName != Capability
DomainAdapter != NewCore
Unknown != Failure
MissingEvidence != NegativeEvidence
InstitutionalOutput != CitizenOutcome
```

## 4. Preserve the citizen language

The original problem remains:

```text
P_C = citizen_problem_verbatim
```

A problem signature is an additional readout, never a replacement.

Example:

```text
P_C:
"The machine starts some mornings but not others."

candidate signature:
intent = IDENTIFY_CAUSE
object_readout = PHYSICAL_SYSTEM
pattern = INTERMITTENT_FAILURE
```

The signature may help routing, but `P_C` remains the auditable source text.

## 5. Candidate signatures, not one forced classification

AI may propose several candidate signatures:

```text
Sigma_cand = {sigma_1, sigma_2, ..., sigma_n}
```

A candidate is not promoted merely because an AI generated it.

Promotion to a working signature requires either citizen endorsement, evidence support, or both, depending on the decision stakes.

```text
P_C
  -> AI candidate translation
  -> citizen/evidence check
  -> Sigma_endorsed
```

If the case cannot yet be classified without distortion, the correct state is `HOLD_UNKNOWN` or `NOT_PROVIDED`.

## 6. Provenance at the facet level

Every material signature facet should retain where it came from.

A facet record uses:

```text
value
provenance[]
confidence
citizen_confirmed
```

Typical provenance values may include:

```text
CITIZEN_VERBATIM
CITIZEN_CLARIFICATION
AI_INFERENCE
WORLD_MEASUREMENT
ORIGINAL_DOCUMENT
EXPERT_RETURN
INSTITUTION_RETURN
```

The vocabulary may evolve, but provenance must remain explicit enough to distinguish observation from translation and inference.

## 7. Problem Signature

A working Problem Signature may contain:

```text
intent
object_readout
observed_difference
evidence_need
stakes
irreversibility
third_party_exposure
authority_need
jurisdiction
candidate_alternatives
next_discriminating_action
citizen_endorsement
```

These are routing coordinates, not metaphysical categories.

The signature does not need every field to be known.

## 8. Barrier Signature

Problem structure and access barriers are separate.

```text
ProblemSignature != BarrierSignature
```

The reference barrier grammar is:

```text
knowledge
skill
language
tool
resource_time
network
credential
permission
opportunity
unknown
```

Each barrier may be:

```text
PRESENT
ABSENT
UNKNOWN
```

This prevents a system from misdiagnosing every difficulty as lack of knowledge or skill.

Examples:

```text
language barrier -> translation may unlock the next action
tool barrier -> more explanation may not help
credential barrier -> capability may exist while legal access does not
permission barrier -> knowledge does not create authority
```

## 9. Practice context

Occupation and practice history remain useful context.

They may carry experiential expertise, terminology, repeated observations, tacit distinctions, or constraints that a generic model does not have.

Therefore:

```text
occupation/practice context
    belongs in CaseContext
```

but:

```text
occupation/practice context
    does not select a bespoke core protocol
```

A mushroom grower, mechanic, teacher, shop owner, software operator, and caregiver may share the same structural operation such as `IDENTIFY_CAUSE`, `COMPARE`, or `VERIFY`, while still carrying very different situated evidence.

## 10. Operational protocol primitives

The compiler may compose from a bounded vocabulary of operations such as:

```text
OBSERVE
DESCRIBE
COMPARE
IDENTIFY
MEASURE
DIAGNOSE
EXPLAIN
VERIFY
TEST
OPTIMIZE
REPAIR
DESIGN
DECIDE
COMPLY
TRANSFER
COORDINATE
VALIDATE
SCALE
```

These are **operations** available to the compiler.

They are not asserted to be the fundamental kinds of all real-world problems.

Runtime action names already implemented by the reference compiler remain unchanged unless a separately governed migration is approved.

## 11. Capability-first routing

The core route should depend on what the case needs done, not on a job title or prestigious provider label.

```text
Problem/Barrier state
    -> Required Capability
    -> Provider capability signature
```

Provider records should increasingly expose concrete capabilities such as:

```text
field inspection
sample analysis
measurement
document interpretation
process audit
expert consultation
licensed judgment
regulatory authorization
prototype support
standards testing
rights/IP support
market matching
```

Country adapters remain responsible for jurisdiction-specific providers and authority constraints.

## 12. Optional domain adapters

Domain adapters are loaded only when the generic core cannot safely or adequately represent a material constraint.

A domain adapter may add:

```text
special vocabulary
known hazards
professional boundaries
special measurements
sample-handling rules
regulatory constraints
domain-specific evidence rules
provider mappings
```

A domain adapter MUST NOT redefine:

```text
P_C preservation
provenance semantics
hard-gate semantics
Case Passport identity
Return Gate semantics
equation authority
```

The intended relationship is:

```text
DomainAdapter = Adapter(Core)
```

not:

```text
DomainAdapter = NewCore
```

## 13. Domain-adapter trigger

Add or load a domain adapter only when at least one of the following is material:

```text
hard safety rule specific to the domain
licensed/professional authority boundary
specialized measurement or sample handling
high-risk ambiguity in terminology
sector-specific regulation or legal authorization
provider ecosystem that requires domain-specific matching
```

A new occupation by itself is not a trigger.

## 14. Context Gap

AI does not have direct access to unrecorded event-specific context.

The signature therefore keeps:

```text
context_known[]
context_unknown[]
```

A system must not silently convert an unobserved context variable into an observed fact.

```text
UnobservedContext != AIInferredFact
```

The next action may be to ask, observe, measure, retrieve an original record, or obtain a human/world-side readout.

## 15. Critical cases and independent routes

For high-stakes or authority-sensitive cases, AI-generated agreement is not sufficient validation.

The existing hard-gate system remains authoritative for runtime behavior.

Where required, the route must include a world-side or independent path such as:

```text
measurement
executed test
original document
licensed professional
laboratory
regulator
independent external human
physical outcome
```

Multiple AI outputs with shared ancestry do not automatically create independence.

## 16. World return

The grammar exists to improve the next justified action, not to finish at classification.

The complete loop is:

```text
Citizen Input
  -> Candidate Signature
  -> Endorsement / unresolved state
  -> Barrier State
  -> Minimal Protocol
  -> Capability Need
  -> Optional Domain Constraint
  -> Provider / Citizen+AI Action
  -> World Readout
  -> Case Event
  -> Updated Passport
```

For external contributions, the existing Return Gate remains mandatory.

For citizen+AI-only local resolution, no artificial institutional Return Object is required; citizen outcome plus satisfied safety/authority constraints may close the case locally.

## 17. Local closure

The reference lifecycle distinguishes:

```text
external_actor_used = false
```

from:

```text
external_actor_used = true
```

A local case may close when:

```text
external_actor_used = false
AND outcome_state is a closure outcome
AND latest_return_gate = NOT_APPLICABLE
```

An externally routed case may close only when:

```text
external_actor_used = true
AND latest_return_gate = PASS
AND outcome_state is a closure outcome
```

This preserves the Return Gate without forcing a fake external return onto a case that never left the citizen+AI/world loop.

## 18. Cross-domain falsification programme

The grammar must earn generality by surviving heterogeneous cases.

Reference testing should sample cases from substantially different contexts, for example:

```text
agriculture
mechanical repair
retail
education
family/community
software
office work
food production
finance
law
health
construction
manufacturing
creative work
```

The test should evaluate whether the unchanged core can:

```text
preserve P_C
represent uncertainty
generate or accept candidate signatures without forced closure
identify the next capability
respect hard safety/authority gates
avoid occupation-specific branching in the core
return to a usable next action
```

A warning sign is repeated pressure to add a new core primitive for every occupation or domain.

A stronger falsifier is:

```text
if abstraction systematically produces worse routing
than preserving and using the original case representation,
reduce or revise the grammar.
```

## 19. Status boundary

This grammar is a platform architecture and machine-contract proposal.

It is not claimed to be:

```text
a universal ontology of reality
a validated psychology of problem solving
a proof that all domains share one mechanism
a replacement for domain expertise
```

Its validity is conditional on auditable use, cross-domain stress testing, and world-side correction.

## 20. Repository boundary

No new Toledo mathematical equation is created by this document.

If future work proposes a new equation or changes an existing equation's meaning, that change belongs in `morrocwi/toledo` under the upstream equation-governance process.

This document governs the product/runtime translation layer only.
