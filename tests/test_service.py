from pathlib import Path

from grokagent.repository import CompanionRepository
from grokagent.service import render_prompt


FIXTURE_PATH = Path(__file__).parents[1] / "data" / "companions.yml"


def test_render_prompt_contains_assets():
    collection = CompanionRepository(FIXTURE_PATH).load()
    prompt_payload = render_prompt(collection, "ani")

    assert "ani" in prompt_payload.rendered_prompt
    assert "persona pack" in prompt_payload.rendered_prompt
    assert "Starter dialogue" in prompt_payload.rendered_prompt


def test_missing_companion_raises():
    collection = CompanionRepository(FIXTURE_PATH).load()
    try:
        render_prompt(collection, "missing")
    except KeyError:
        return
    assert False, "Expected KeyError for missing companion"
