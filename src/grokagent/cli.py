from __future__ import annotations

from pathlib import Path
import typer

from .repository import CompanionRepository
from .service import render_prompt

app = typer.Typer(help="Local helper for loading Grok companion prompts")


@app.command()
def list(path: Path = typer.Option(Path("data/companions.yml"), exists=True, readable=True)):
    """List available companion ids and summaries."""
    collection = CompanionRepository(path).load()
    for companion in collection.companions:
        typer.echo(f"{companion.id}\t{companion.name}\t{companion.summary}")


@app.command()
def prompt(
    companion_id: str,
    path: Path = typer.Option(Path("data/companions.yml"), exists=True, readable=True),
):
    """Render a companion's prompt payload for pasting into Grok."""
    collection = CompanionRepository(path).load()
    prompt_payload = render_prompt(collection, companion_id)
    typer.echo(prompt_payload.rendered_prompt)


if __name__ == "__main__":
    app()
