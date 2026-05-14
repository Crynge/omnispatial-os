from __future__ import annotations

import math

from .models import SpatialZone


def occupancy_similarity(zone: SpatialZone, target: tuple[float, float, float]) -> float:
    vector = [zone.foot_traffic_index / 100, zone.wifi_occupancy, zone.event_heat]
    numerator = sum(a * b for a, b in zip(vector, target))
    denom = math.sqrt(sum(a * a for a in vector)) * math.sqrt(sum(b * b for b in target))
    if denom == 0:
        return 0.0
    return round(numerator / denom, 4)


def hyperlocal_pressure(zone: SpatialZone) -> float:
    pressure = (
        zone.foot_traffic_index * 0.32
        + zone.event_heat * 42
        + zone.competitor_activity * 19
        - zone.weather_pressure * 14
    )
    return round(pressure, 2)

