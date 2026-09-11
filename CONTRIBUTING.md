# Contributing

Thank you for contributing to Toledo Citizen Platform.

## Before opening a change

Please identify which layer you are changing:

```text
citizen UX
case schema
safety / escalation
institution routing
cross-actor continuity
country adapter
localization
implementation code
documentation
```

If the change depends on a Toledo equation, verify the canonical source in:

`https://github.com/morrocwi/toledo`

Do not introduce a new equation here as though it were canonical.

## Pull-request expectations

A change that affects routing or governance should state:

- the case state it changes;
- which hard gates are affected;
- expected citizen benefit;
- failure mode introduced or reduced;
- privacy/rights implications;
- migration impact on existing Case Passports;
- equation references when applicable.

## Safety-sensitive changes

Changes affecting health, legal, regulatory, financial, physical-safety, or irreversible-action routing require explicit tests for:

```text
hard escalation
unknown state
fallback route
response-time fit
return-to-citizen
```

Never replace a hard gate with a soft score.

## Institution data

Institution records must include a public source and `last_verified` date.

Do not mark a program as currently available from historical evidence alone.

## Privacy

Do not include real citizen case data in fixtures unless it has been deliberately synthetic or irreversibly anonymized.

Never commit:

- identity documents;
- medical records;
- private addresses;
- credentials/secrets;
- confidential contracts;
- sensitive community data.

## Documentation style

Prefer:

- explicit definitions;
- non-collapse statements;
- typed states;
- examples;
- traceable source boundaries.

Avoid language that turns AI into a truth authority or institutions into a mandatory hierarchy.

## License

By contributing, you agree that software contributions are MIT-licensed and documentation/specification contributions are CC BY 4.0 unless a file states otherwise.
