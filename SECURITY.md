# Security and Sensitive-Case Policy

## Public repository boundary

This GitHub repository is public infrastructure and documentation. It is **not** an approved storage location for real citizen case data.

Do not submit sensitive case material through public issues, pull requests, discussions, examples, screenshots, logs, or fixtures.

Sensitive material includes, at minimum:

- medical and health records;
- identity documents;
- exact private addresses;
- passwords, tokens, API keys, or account credentials;
- private legal or financial records;
- confidential business data;
- unpublished patent-sensitive information;
- community knowledge subject to consent or benefit-sharing restrictions.

## Reporting software vulnerabilities

Do not disclose exploitable security vulnerabilities in a public issue.

Use a private maintainer contact or GitHub private vulnerability reporting when it is enabled for this repository.

## Product implementation requirements

A production implementation should separate:

```text
public code/specification
from
private citizen case storage
```

Production deployments should implement:

- data minimization;
- explicit consent scopes;
- role-based access control;
- encryption in transit and at rest;
- audit logs;
- retention/deletion policy;
- secret management;
- jurisdiction-specific privacy controls;
- safe redaction/export of Case Passport views.

## AI boundary

Prompts, model outputs, and tool traces may themselves contain sensitive information. Production systems should treat them as governed case data rather than harmless application logs.

## Institution handoffs

Before transmitting case data to an external institution, verify:

```text
consent scope
data-use purpose
minimum necessary data
recipient identity
return obligation
retention expectations
```

A valid route is not automatically a valid data transfer.
