from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class SpatialZone:
    zone_id: str
    name: str
    city: str
    foot_traffic_index: float
    weather_pressure: float
    competitor_activity: float
    wifi_occupancy: float
    event_heat: float
    local_roi_score: float

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class AgentRecommendation:
    agent: str
    zone_id: str
    action: str
    confidence: float
    rationale: str

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class SignalHealth:
    name: str
    freshness_minutes: int
    health_score: float
    fallback_mode: str

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)

