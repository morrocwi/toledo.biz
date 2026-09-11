# ADR 0005 — Anchor-Preserved Decision Threads

Status: **accepted for reference runtime**  
Date: 2026-09-11

## Context

The original Toledo runtime represented one Case Passport with one `current_phase` and one `current_decision`. Cross-domain tests showed that this is sufficient for simple local cases but not for many real cases in which several decisions coexist at different routing phases.

Example: one cosmetics business case may simultaneously contain:

- a quality-cause decision at P1;
- an external testing decision at P3;
- a regulatory/claim decision under a regulatory overlay;
- a scale decision at P10 that should wait for earlier decisions.

Creating a new domain-specific phase or replacing P0-P11 would violate Toledo's anchor-preserving design.

## Decision

Preserve the existing Case Passport, P0-P11 phase semantics, Protocol Compiler, Problem Signature, hard gates, Return Gate and equation bindings.

Add a **Decision Thread** as a decision-specific subgraph inside the same Case Passport:

```text
Case Passport
  ├── P_C / citizen goal / shared context
  ├── Decision Thread T1 -> phase / evidence / gates / capability
  ├── Decision Thread T2 -> phase / evidence / gates / capability
  └── Decision Thread T3 -> phase / evidence / gates / capability
```

Formally, the runtime representation becomes:

```text
Case = {shared_case_state, T1, T2, ..., Tn}
```

where each `Tj` is an operational object, not a new Toledo equation or a new maturity scale.

The old fields remain as a **primary-thread projection**:

```text
current_phase    = primary_thread.phase
current_decision = primary_thread.decision
```

This preserves backward compatibility for callers that understand only the original single-decision contract.

## Dependency rule

A thread may declare `depends_on` other thread IDs. If a dependency is not `CLOSED` or `CANCELLED`, the dependent thread is `BLOCKED` and its protocol emits a hold rather than pretending that the downstream decision is ready.

Hard safety/authority escalation remains higher priority than a dependency hold.

## Closure rule

Thread closure is decision-local. Case closure remains citizen-level.

- a local thread may close without a Return Object when no external actor was used and no hard escalation remains;
- an external thread requires a passing Return Gate before it may close;
- a case with multiple required threads does not close until all required non-cancelled threads are closed and the citizen-level outcome condition is satisfied.

## Non-collapse rules

```text
Case != SingleDecision
DecisionThread != NewCase
ThreadPhase != CaseMaturity
BlockedThread != FailedCase
ThreadClosure != CaseClosure
BusinessPhase != SafetyPhase
RegulatoryOverlay != BusinessMaturity
```

## Consequences

Positive:

- P0-P11 are retained rather than rewritten;
- complex real-life cases can be decomposed without multiplying domain-specific protocols;
- dependencies such as `quality -> regulatory -> scale` can be explicit and auditable;
- AI agents can reason over several decision subgraphs while preserving one citizen problem and one Case Passport.

Costs:

- schemas and runtime must carry thread-local evidence, gates and outcomes;
- routing UIs must distinguish case-level and thread-level state;
- legacy fields require synchronization with the primary thread.

## Authority boundary

This ADR is a product/runtime architecture decision in `toledo.biz`. It does not create or promote a mathematical equation in `morrocwi/toledo`.
