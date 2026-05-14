from __future__ import annotations

from .agents import budget_agent, creative_agent, ops_agent, trend_agent
from .causal import simulate_roi
from .models import AgentRecommendation
from .sample_data import sample_signals, sample_zones
from .spatial import hyperlocal_pressure


class OmniSpatialOS:
    def __init__(self) -> None:
        self.zones = sample_zones()
        self.signals = sample_signals()

    def overview(self) -> dict:
        avg_roi = round(sum(zone.local_roi_score for zone in self.zones) / len(self.zones), 2)
        avg_signal = round(sum(signal.health_score for signal in self.signals) / len(self.signals), 2)
        hottest = max(self.zones, key=hyperlocal_pressure)
        return {
            "physical_roi_index": avg_roi,
            "signal_health_index": avg_signal,
            "top_zone": hottest.as_dict(),
            "zone_count": len(self.zones),
            "signal_count": len(self.signals),
        }

    def zones_panel(self) -> list[dict]:
        rows: list[dict] = []
        for zone in self.zones:
            rows.append({**zone.as_dict(), "pressure_score": hyperlocal_pressure(zone)})
        return rows

    def agents_panel(self) -> list[dict]:
        items: list[AgentRecommendation] = [
            trend_agent(self.zones),
            creative_agent(self.zones),
            budget_agent(self.zones),
            ops_agent(self.zones),
        ]
        return [item.as_dict() for item in items]

    def signals_panel(self) -> list[dict]:
        return [signal.as_dict() for signal in self.signals]

    def what_if(self, budget_shift_pct: float, weather_index: float, event_heat: float, competitor_activity: float) -> dict:
        result = simulate_roi(budget_shift_pct, weather_index, event_heat, competitor_activity)
        result["narrative"] = (
            "The model predicts the strongest hyperlocal lift when budget moves are paired with event heat and "
            "tempered against weather friction and competitor density."
        )
        return result

