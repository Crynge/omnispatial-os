pub fn normalize_wifi_occupancy(raw_signal: f64) -> f64 {
    (raw_signal / 100.0).clamp(0.0, 1.0)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn wifi_signal_is_clamped() {
        assert_eq!(normalize_wifi_occupancy(140.0), 1.0);
    }
}

