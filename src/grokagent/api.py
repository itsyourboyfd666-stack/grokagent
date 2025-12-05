from __future__ import annotations

from fastapi import Depends, FastAPI, HTTPException

from .models import Companion, CompanionPrompt, CompanionCollection
from .repository import CompanionRepository
from .service import render_prompt


def get_repository() -> CompanionRepository:
    return CompanionRepository(path="data/companions.yml")


def load_companions(repo: CompanionRepository = Depends(get_repository)) -> CompanionCollection:
    return repo.load()


app = FastAPI(title="Grok Companion Registry")


@app.get("/companions", response_model=list[Companion])
def list_companions(collection: CompanionCollection = Depends(load_companions)) -> list[Companion]:
    return collection.companions


@app.get("/companions/{companion_id}", response_model=Companion)
def get_companion(companion_id: str, collection: CompanionCollection = Depends(load_companions)) -> Companion:
    companion = collection.get(companion_id)
    if not companion:
        raise HTTPException(status_code=404, detail="Companion not found")
    return companion


@app.get("/companions/{companion_id}/prompt", response_model=CompanionPrompt)
def get_companion_prompt(
    companion_id: str, collection: CompanionCollection = Depends(load_companions)
) -> CompanionPrompt:
    try:
        return render_prompt(collection, companion_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Companion not found")


@app.get("/health")
def healthcheck():
    return {"status": "ok"}
