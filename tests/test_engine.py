from src.omnispatial_os import OmniSpatialOS


def test_overview_has_indices() -> None:
    engine = OmniSpatialOS()
    overview = engine.overview()
    assert overview["physical_roi_index"] > 0
    assert overview["signal_health_index"] > 0


def test_what_if_has_confidence_bounds() -> None:
    engine = OmniSpatialOS()
    result = engine.what_if(12, 0.3, 0.7, 0.4)
    assert result["confidence_low"] < result["confidence_high"]

