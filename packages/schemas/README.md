# Toledo Citizen Platform Schemas

Machine-readable contracts live here.

## Current schemas

| Schema | Purpose |
|---|---|
| `case-passport.schema.json` | Persistent cross-actor case state, Decision Threads and event history |
| `decision-thread.schema.json` | One decision-specific routing subgraph inside a Case Passport |
| `case-event.schema.json` | One auditable state transition; supported events may be scoped by `thread_id` |
| `case-step-request.schema.json` | Stateless initialize/update/recompile request |
| `case-step-response.schema.json` | Updated Case Passport plus primary protocol and all Decision Thread protocols |
| `problem-signature.schema.json` | Domain-neutral candidate problem signatures, facet provenance, context gaps, barriers and domain-adapter need |
| `return-object.schema.json` | Structured return from expert/institution to citizen/decision owner |
| `institution-record.schema.json` | Capability-bearing public/university/institution mechanism |
| `country-adapter-manifest.schema.json` | Country adapter identity, compatibility and dataset manifest |
| `protocol-compile-request.schema.json` | Compact direct Protocol Compiler input |
| `protocol-instance.schema.json` | Deterministic next-action readout, including dependency holds and thread metadata |

## Authority

For object shape, these schemas are machine-readable contracts. Normative behavior is in `docs/`. Mathematical equations are authoritative only in `morrocwi/toledo` and are referenced through `docs/EQUATION_BINDINGS.md`.

`problem-signature.schema.json` is an implementation contract for a routing readout. It is not a claim that its fields exhaust all real-world problems or form a validated universal ontology.

`decision-thread.schema.json` is a runtime orchestration contract. It does not create a new Toledo equation and does not replace the P0-P11 phase definitions.

## Anchor-preserved relation

```text
Citizen Problem / P_C
  → Case Passport
      ├── shared context / rights / provenance
      ├── Decision Thread T1
      ├── Decision Thread T2
      └── Decision Thread Tn
  → Case Event*
  → Case Step Request
  → primary Protocol Instance + thread_protocols[]
  → World / Institution
  → Return Object / Case Event
  → next Case Passport version
```

Existing single-decision callers remain supported because the runtime creates one primary Decision Thread automatically and projects it back to:

```text
current_phase
current_decision
```

## Decision dependency rule

A Decision Thread may carry:

```text
depends_on[]
blocking_threads[]
```

If dependencies are unresolved, the thread is blocked and the compiler emits `HOLD` / `HOLD_FOR_DEPENDENCY`, unless a hard safety/authority gate requires escalation first.

```text
HardSafetyEscalation > DependencyHold
```

## Provenance rule

Material Problem Signature facets should carry provenance sufficient to distinguish citizen wording, AI inference, world measurement, original records and external returns where relevant.

```text
AITranslation != CitizenObservation
ProblemSignature != Diagnosis
CandidateSignature != EndorsedSignature
```

Unknown and unresolved states are valid machine outputs.

## Validation

CI validates all Draft 2020-12 schemas, reference adapter data, equation mirror integrity, runtime-generated Case Passports and Decision Threads, Problem Signature fixtures, cross-domain multi-decision regression tests, runtime unit tests and service imports.

## Privacy

Schemas define structure, not permission to store data publicly. Real Case Passports, Decision Threads and Return Objects may contain sensitive data and must live only in appropriately private deployments.
