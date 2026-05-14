from __future__ import annotations

from .models import AgentRecommendation, SpatialZone
from .spatial import hyperlocal_pressure, occupancy_similarity


def trend_agent(zones: list[SpatialZone]) -> AgentRecommendation:
    zone = max(zones, key=hyperlocal_pressure)
    return AgentRecommendation(
        agent="TrendAgent",
        zone_id=zone.zone_id,
        action=f"Escalate hyperlocal push around {zone.name} before evening demand peaks.",
        confidence=0.87,
        rationale="Physical demand pressure and event heat are rising faster than competitor saturation.",
    )


def creative_agent(zones: list[SpatialZone]) -> AgentRecommendation:
    zone = max(zones, key=lambda item: occupancy_similarity(item, (0.88, 0.74, 0.66)))
    return AgentRecommendation(
        agent="CreativeAgent",
        zone_id=zone.zone_id,
        action=f"Generate culturally-tuned street-level dining creatives for {zone.name}.",
        confidence=0.82,
        rationale="Occupancy and event similarity match the strongest social conversion archetype.",
    )


def budget_agent(zones: list[SpatialZone]) -> AgentRecommendation:
    zone = max(zones, key=lambda item: item.local_roi_score - item.competitor_activity * 8)
    return AgentRecommendation(
        agent="BudgetAgent",
        zone_id=zone.zone_id,
        action=f"Shift incremental budget toward {zone.name} and reduce spend in weaker spillover clusters.",
        confidence=0.84,
        rationale="Modeled local ROI remains high even after competitor drag is applied.",
    )


def ops_agent(zones: list[SpatialZone]) -> AgentRecommendation:
    zone = max(zones, key=lambda item: item.competitor_activity + item.weather_pressure)
    return AgentRecommendation(
        agent="OpsAgent",
        zone_id=zone.zone_id,
        action=f"Activate resilient fallback playbooks for {zone.name} due to elevated context volatility.",
        confidence=0.79,
        rationale="Weather and competitor noise are high enough to warrant guarded execution and monitoring.",
    )

