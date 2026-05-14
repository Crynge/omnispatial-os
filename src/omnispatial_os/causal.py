from __future__ import annotations


def simulate_roi(budget_shift_pct: float, weather_index: float, event_heat: float, competitor_activity: float) -> dict[str, float]:
    local_lift = round(budget_shift_pct * 0.54 + event_heat * 18 - competitor_activity * 9 - weather_index * 6, 2)
    offline_roi = round(2.1 + local_lift * 0.04, 2)
    online_spillover = round(local_lift * 0.31, 2)
    confidence_low = round(offline_roi - 0.28, 2)
    confidence_high = round(offline_roi + 0.36, 2)
    return {
        "local_lift_pct": local_lift,
        "offline_roi": offline_roi,
        "online_spillover_pct": online_spillover,
        "confidence_low": confidence_low,
        "confidence_high": confidence_high,
    }

