# `apps/steward-console`

Workspace for the Civic Knowledge Case Steward.

The steward coordinates the case but is not the truth authority.

Core views:

- active Case Passports;
- current phase / current decision;
- requested capability;
- consent and data-use scope;
- institution / expert match;
- academic-fit vs university-executability status;
- handoff validation;
- response deadline / time-fit risk;
- fallback route;
- pending Return Objects;
- return-gate failures;
- rights / provenance state;
- failed-route history.

The console should make the following failures highly visible:

```text
meaning drift
referral without handoff
no decision owner
institution cannot execute
consent mismatch
rights ambiguity
response-time failure
no return to citizen
repeated re-telling burden
```

The steward may coordinate, request status, request returns, and reroute within authorized scope. The steward does not become a regulator, professional authority, IP owner, or expert merely by holding the case.
