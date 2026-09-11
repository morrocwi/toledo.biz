# `apps/citizen-web`

Citizen-facing application.

The UI should feel much simpler than the back-end framework.

Primary flow:

```text
Tell us the problem in your own words
    ↓
What did you observe?
    ↓
What have you already tried?
    ↓
What are you trying to achieve?
    ↓
AI structures the case
    ↓
Citizen confirms / corrects meaning
    ↓
Platform explains the next safest useful step
```

Required product behaviors:

- preserve the verbatim citizen problem;
- visibly distinguish observation from interpretation;
- explain why escalation is or is not needed;
- explain why a specific capability/institution is suggested;
- never imply that AI certainty substitutes for professional authority;
- show the citizen who currently has the case;
- show deadlines / expected return when known;
- render Return Objects in plain language;
- support multilingual input without replacing the original wording;
- provide clear privacy boundaries before sensitive information is entered.

Real case data must live in a private deployment, not in this public GitHub repository.
