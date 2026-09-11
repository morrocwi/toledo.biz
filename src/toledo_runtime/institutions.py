from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


_ACCESS_RANK = {"A4": 4, "A3": 3, "A2": 2, "A1": 1, "A0": 0}


class InstitutionStore:
    """Reference institution lookup.

    v0.2 ships the Thailand reference adapter. Other jurisdictions should be
    added through the country-adapter contract rather than hard-coded here.
    """

    def __init__(self, root: str | Path | None = None) -> None:
        self.root = Path(root) if root else _repo_root()

    def _load(self, jurisdiction: str) -> list[dict[str, Any]]:
        code = jurisdiction.strip().upper()
        if code in {"TH", "THA", "THAILAND"}:
            path = self.root / "adapters" / "thailand" / "institutions.seed.json"
            return json.loads(path.read_text(encoding="utf-8"))
        return []

    def route(
        self,
        *,
        jurisdiction: str = "TH",
        phase: str | None = None,
        capability: str | None = None,
        target_user: str | None = None,
        limit: int = 5,
    ) -> list[dict[str, Any]]:
        cap = (capability or "").lower().strip()
        target = (target_user or "").lower().strip()
        candidates: list[dict[str, Any]] = []
        for record in self._load(jurisdiction):
            if phase and phase not in record.get("phase_fit", []):
                continue
            if cap:
                hay = " ".join(record.get("capability", []) + record.get("service_type", [])).lower()
                if cap not in hay:
                    continue
            if target and target not in {str(x).lower() for x in record.get("target_user", [])}:
                continue
            candidates.append(record)
        candidates.sort(
            key=lambda r: (
                _ACCESS_RANK.get(r.get("citizen_accessibility", "A0"), 0),
                r.get("last_verified", ""),
            ),
            reverse=True,
        )
        return candidates[: max(1, min(limit, 25))]
