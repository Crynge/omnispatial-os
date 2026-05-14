from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.omnispatial_os import OmniSpatialOS


class WhatIfRequest(BaseModel):
    budget_shift_pct: float
    weather_index: float
    event_heat: float
    competitor_activity: float


app = FastAPI(title="OmniSpatial OS", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = OmniSpatialOS()


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "omnispatial-os"}


@app.get("/api/overview")
def overview() -> dict:
    return engine.overview()


@app.get("/api/zones")
def zones() -> dict:
    return {"items": engine.zones_panel()}


@app.get("/api/agents")
def agents() -> dict:
    return {"items": engine.agents_panel()}


@app.get("/api/signals")
def signals() -> dict:
    return {"items": engine.signals_panel()}


@app.post("/api/what-if")
def what_if(payload: WhatIfRequest) -> dict:
    return engine.what_if(payload.budget_shift_pct, payload.weather_index, payload.event_heat, payload.competitor_activity)


@app.post("/api/train")
def train() -> dict:
    return {"status": "noop", "message": "Lite build uses deterministic spatial policies for demo verification."}

