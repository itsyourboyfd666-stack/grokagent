from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, HttpUrl, Field


class ExternalAssets(BaseModel):
    script_url: HttpUrl = Field(..., description="URL to the companion's executable script")
    config_url: HttpUrl = Field(..., description="URL to configuration JSON or YAML")
    persona_pack_url: HttpUrl = Field(..., description="URL to markdown persona pack")


class StarterMessage(BaseModel):
    role: str
    content: str


class Companion(BaseModel):
    id: str
    name: str
    summary: str
    system_prompt: str
    traits: List[str]
    external_assets: ExternalAssets
    starter_messages: List[StarterMessage]


class CompanionPrompt(BaseModel):
    companion_id: str
    name: str
    summary: str
    system_prompt: str
    traits: List[str]
    external_assets: ExternalAssets
    starter_messages: List[StarterMessage]
    rendered_prompt: str


class CompanionCollection(BaseModel):
    companions: List[Companion]

    def get(self, companion_id: str) -> Optional[Companion]:
        return next((c for c in self.companions if c.id == companion_id), None)
