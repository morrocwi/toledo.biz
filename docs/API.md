# Toledo Protocol API

The reference API exposes the Protocol Compiler, equation readouts, institution routing, handoff validation and Return Gate validation.

## Run

```bash
python -m pip install -e .
toledo-api
```

Default development address: `http://127.0.0.1:8787`.

FastAPI also exposes generated OpenAPI at `/openapi.json` and interactive docs at `/docs`.

A repository-controlled contract is stored at `openapi/toledo.protocol.v1.yaml`.

## Endpoints

```text
GET  /health
GET  /.well-known/toledo
GET  /v1/equations
GET  /v1/equations/{equation_id}
POST /v1/protocols/compile
GET  /v1/institutions
POST /v1/handoffs/validate
POST /v1/returns/validate
GET  /v1/schemas/{schema_name}
```

### Equations

`GET /v1/equations?domain=cross_actor&q=handoff`

Use `live=true` to attempt a read from the pinned upstream Toledo commit. Failure falls back to the local auditable mirror and is disclosed in the response.

### Compile

```bash
curl -X POST http://127.0.0.1:8787/v1/protocols/compile \
  -H 'content-type: application/json' \
  -d '{"problem":"Water pools in one part of my orchard","phase":"P0","jurisdiction":"TH"}'
```

The API is stateless in this reference implementation. Production deployments need authenticated private case storage and audit logging.
