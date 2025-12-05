from __future__ import annotations

from typing import List

from .models import CompanionCollection, CompanionPrompt


PROMPT_HEADER = """You are loading a Grok companion from an external registry.\n"""

PROMPT_TEMPLATE = """[Companion: {name}]\nSummary: {summary}\nTraits: {traits}\nExternal assets:\n  script: {script_url}\n  config: {config_url}\n  persona pack: {persona_pack_url}\n---\nSystem prompt:\n{system_prompt}\n---\nStarter dialogue:\n{starter}\n"""


def render_prompt(companion_collection: CompanionCollection, companion_id: str) -> CompanionPrompt:
    companion = companion_collection.get(companion_id)
    if not companion:
        raise KeyError(f"Companion '{companion_id}' not found")

    starter_lines: List[str] = []
    for message in companion.starter_messages:
        starter_lines.append(f"{message.role}: {message.content}")
    starter_block = "\n".join(starter_lines)

    prompt_body = PROMPT_TEMPLATE.format(
        name=companion.name,
        summary=companion.summary,
        traits=", ".join(companion.traits),
        script_url=companion.external_assets.script_url,
        config_url=companion.external_assets.config_url,
        persona_pack_url=companion.external_assets.persona_pack_url,
        system_prompt=companion.system_prompt.strip(),
        starter=starter_block,
    )

    rendered = PROMPT_HEADER + prompt_body

    return CompanionPrompt(
        companion_id=companion.id,
        name=companion.name,
        summary=companion.summary,
        system_prompt=companion.system_prompt,
        traits=companion.traits,
        external_assets=companion.external_assets,
        starter_messages=companion.starter_messages,
        rendered_prompt=rendered,
    )
