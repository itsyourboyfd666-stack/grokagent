from __future__ import annotations

import yaml
from pathlib import Path
from typing import Union

from .models import CompanionCollection


class CompanionRepository:
    def __init__(self, path: Union[str, Path]):
        self.path = Path(path)

    def load(self) -> CompanionCollection:
        if not self.path.exists():
            raise FileNotFoundError(f"Companion registry not found: {self.path}")
        with self.path.open("r", encoding="utf-8") as handle:
            payload = yaml.safe_load(handle) or {}
        try:
            return CompanionCollection.model_validate(payload)
        except Exception as exc:  # pragma: no cover - pydantic already provides detail
            raise ValueError(f"Invalid companion data in {self.path}: {exc}")
