from __future__ import annotations

from .models import SignalHealth, SpatialZone


def sample_zones() -> list[SpatialZone]:
    return [
        SpatialZone("blr_koramangala_5", "Koramangala 5th Block", "Bengaluru", 88, 0.24, 0.56, 0.74, 0.68, 81.2),
        SpatialZone("mum_bkc_north", "BKC North Loop", "Mumbai", 79, 0.36, 0.48, 0.69, 0.61, 76.8),
        SpatialZone("del_cp_inner", "Connaught Inner Circle", "Delhi", 72, 0.21, 0.63, 0.66, 0.59, 73.1),
        SpatialZone("hyd_hitech_gateway", "Hitech Gateway", "Hyderabad", 69, 0.18, 0.34, 0.58, 0.47, 71.6),
    ]


def sample_signals() -> list[SignalHealth]:
    return [
        SignalHealth("WiFi CSI", 3, 91.0, "none"),
        SignalHealth("Satellite ViT", 19, 84.0, "classical-imagery-model"),
        SignalHealth("Weather Feed", 1, 97.0, "none"),
        SignalHealth("Competitor Watch", 12, 78.0, "cached-open-data"),
    ]

