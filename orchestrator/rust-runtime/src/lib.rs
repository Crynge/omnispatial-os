pub struct Route {
    pub channel: &'static str,
    pub urgency: u8,
}

pub fn route_agent_signal(pressure: f64, health: f64) -> Route {
    if pressure > 38.0 && health > 80.0 {
        Route { channel: "launch", urgency: 9 }
    } else {
        Route { channel: "review", urgency: 6 }
    }
}

