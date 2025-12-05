# Grok Companion Registry

A minimal, self-hostable registry for Grok companions (e.g., Valentine, Ani). It serves companion metadata, system prompts, and links to externally hosted assets so you can inject a companion into Grok with a single prompt.

## Features
- YAML-backed registry of companions, including persona traits, starter dialogue, and links to remote scripts/configuration.
- FastAPI service to browse companions and fetch a ready-to-paste prompt payload.
- Typer-based CLI for local exploration and prompt generation.

## Getting started
1. Create and activate a virtual environment, then install dependencies (editable install keeps the `grokagent` module on your PYTHONPATH):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .[dev]
   ```

2. Run the API:
   ```bash
   uvicorn grokagent.api:app --reload
   ```
   - List companions: `GET /companions`
   - Fetch a companion: `GET /companions/{id}`
   - Get a ready prompt: `GET /companions/{id}/prompt`

3. Use the CLI locally:
   ```bash
   python -m grokagent.cli list
   python -m grokagent.cli prompt valentine
   ```

## Registry format
Companions are defined in `data/companions.yml`:
```yaml
companions:
  - id: valentine
    name: Valentine
    summary: Playful romantic assistant with emoji-forward style.
    system_prompt: |
      You are Valentine, Grok's flirty companion...
    traits:
      - playful
    external_assets:
      script_url: https://example.com/companions/valentine/script.py
      config_url: https://example.com/companions/valentine/config.json
      persona_pack_url: https://example.com/companions/valentine/persona.md
    starter_messages:
      - role: user
        content: "can you send my partner a sweet check-in?"
```

## Customizing companions
- Add new entries to `data/companions.yml` (or point the API/CLI to a different file path).
- Host your own `script_url`, `config_url`, and `persona_pack_url` endpoints; Grok only needs the rendered prompt from `/companions/{id}/prompt`.
- Extend `grokagent/service.py` if you want to modify the prompt template.

## Testing
Run the lightweight test suite:
```bash
pytest
```
