from __future__ import annotations

import httpx


def main() -> int:
    base = "http://127.0.0.1:8036"
    with httpx.Client(timeout=20.0) as client:
        health = client.get(f"{base}/health")
        overview = client.get(f"{base}/api/overview")
        scenario = client.post(
            f"{base}/api/what-if",
            json={"budget_shift_pct": 9, "weather_index": 0.24, "event_heat": 0.7, "competitor_activity": 0.46},
        )
    assert health.status_code == 200
    assert overview.status_code == 200
    assert scenario.status_code == 200
    assert "offline_roi" in scenario.json()
    print("api smoke passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

