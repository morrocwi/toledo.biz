from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

UPSTREAM_REPO = "morrocwi/toledo"
UPSTREAM_PATH = "registry/proposals/TOLEDO_CITIZEN_BRIDGE_v0.17.json"
UPSTREAM_COMMIT = "361546c934829de56f3dcff2032c740209de847a"
UPSTREAM_RAW = (
    "https://raw.githubusercontent.com/morrocwi/toledo/"
    + UPSTREAM_COMMIT
    + "/"
    + UPSTREAM_PATH
)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


class EquationStore:
    """Read-only equation access with an auditable local mirror and live option.

    The local index is a convenience cache, never the mathematical authority.
    Every response carries upstream provenance and status.
    """

    def __init__(self, index_path: str | Path | None = None) -> None:
        self.index_path = Path(
            index_path
            or os.getenv("TOLEDO_EQUATION_INDEX", "")
            or (_repo_root() / "registry" / "equation-index.json")
        )
        self._data = self._load_local()

    def _load_local(self) -> dict[str, Any]:
        return json.loads(self.index_path.read_text(encoding="utf-8"))

    def load_live(self, timeout: float = 5.0) -> dict[str, Any]:
        req = Request(UPSTREAM_RAW, headers={"User-Agent": "toledo-citizen-runtime/0.2"})
        with urlopen(req, timeout=timeout) as response:
            upstream = json.loads(response.read().decode("utf-8"))
        return {
            "registry_id": upstream.get("registry_id"),
            "registry_status": upstream.get("registry_status"),
            "source": {
                "repo": UPSTREAM_REPO,
                "path": UPSTREAM_PATH,
                "commit": UPSTREAM_COMMIT,
                "authority": "upstream",
            },
            "entries": upstream.get("entries", []),
        }

    def data(self, live: bool = False) -> dict[str, Any]:
        if live:
            try:
                return self.load_live()
            except Exception as exc:  # deterministic fallback with disclosure
                data = dict(self._data)
                data["live_fetch"] = {"ok": False, "fallback": "local_mirror", "error": str(exc)}
                return data
        return self._data

    def list(
        self,
        *,
        domain: str | None = None,
        status: str | None = None,
        live: bool = False,
    ) -> list[dict[str, Any]]:
        entries = self.data(live=live).get("entries", [])
        return [
            e
            for e in entries
            if (domain is None or e.get("domain") == domain)
            and (status is None or e.get("status") == status)
        ]

    def get(self, equation_id: str, *, live: bool = False) -> dict[str, Any] | None:
        for entry in self.list(live=live):
            if entry.get("id") == equation_id:
                return {
                    **entry,
                    "source_repo": UPSTREAM_REPO,
                    "source_path": UPSTREAM_PATH,
                    "source_commit": UPSTREAM_COMMIT,
                    "authority": "upstream Toledo; local response is a bound readout",
                }
        return None

    def search(self, query: str = "", *, domain: str | None = None, live: bool = False) -> list[dict[str, Any]]:
        q = query.strip().lower()
        out: list[dict[str, Any]] = []
        for entry in self.list(domain=domain, live=live):
            haystack = " ".join(
                str(entry.get(k, "")) for k in ("id", "name", "kind", "domain", "statement")
            ).lower()
            if not q or q in haystack:
                out.append(entry)
        return out
