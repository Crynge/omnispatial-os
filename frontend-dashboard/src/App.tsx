import { useEffect, useState } from "react";

type Zone = {
  zone_id: string;
  name: string;
  city: string;
  local_roi_score: number;
  pressure_score: number;
  competitor_activity: number;
  weather_pressure: number;
};

type Agent = {
  agent: string;
  zone_id: string;
  action: string;
  confidence: number;
  rationale: string;
};

type Overview = {
  physical_roi_index: number;
  signal_health_index: number;
  top_zone: {
    name: string;
    city: string;
  };
  zone_count: number;
  signal_count: number;
};

const fallbackOverview: Overview = {
  physical_roi_index: 75.7,
  signal_health_index: 87.5,
  top_zone: { name: "Koramangala 5th Block", city: "Bengaluru" },
  zone_count: 4,
  signal_count: 4
};

const fallbackZones: Zone[] = [
  {
    zone_id: "blr_koramangala_5",
    name: "Koramangala 5th Block",
    city: "Bengaluru",
    local_roi_score: 81.2,
    pressure_score: 42.5,
    competitor_activity: 0.56,
    weather_pressure: 0.24
  },
  {
    zone_id: "mum_bkc_north",
    name: "BKC North Loop",
    city: "Mumbai",
    local_roi_score: 76.8,
    pressure_score: 37.7,
    competitor_activity: 0.48,
    weather_pressure: 0.36
  }
];

const fallbackAgents: Agent[] = [
  {
    agent: "TrendAgent",
    zone_id: "blr_koramangala_5",
    action: "Escalate hyperlocal push around Koramangala 5th Block before evening demand peaks.",
    confidence: 0.87,
    rationale: "Physical demand pressure and event heat are rising faster than competitor saturation."
  },
  {
    agent: "BudgetAgent",
    zone_id: "mum_bkc_north",
    action: "Shift incremental budget toward BKC North Loop and reduce spend in weaker spillover clusters.",
    confidence: 0.84,
    rationale: "Modeled local ROI remains high even after competitor drag is applied."
  }
];

function App() {
  const apiBase = (import.meta.env.VITE_API_BASE as string | undefined) ?? "http://127.0.0.1:8036";
  const [overview, setOverview] = useState<Overview>(fallbackOverview);
  const [zones, setZones] = useState<Zone[]>(fallbackZones);
  const [agents, setAgents] = useState<Agent[]>(fallbackAgents);

  useEffect(() => {
    Promise.all([
      fetch(`${apiBase}/api/overview`).then((res) => res.json()),
      fetch(`${apiBase}/api/zones`).then((res) => res.json()),
      fetch(`${apiBase}/api/agents`).then((res) => res.json())
    ])
      .then(([nextOverview, nextZones, nextAgents]) => {
        setOverview(nextOverview);
        setZones(nextZones.items);
        setAgents(nextAgents.items);
      })
      .catch(() => {
        // offline demo fallback
      });
  }, [apiBase]);

  return (
    <main className="shell">
      <section className="hero">
        <div className="hero-copy">
          <p className="eyebrow">OmniSpatial Command Mesh</p>
          <h1>Cities become programmable when spatial signals, local culture, and agent swarms work together.</h1>
          <p className="lede">
            OmniSpatial OS interprets foot traffic, weather, competitor activity, and edge occupancy signals to give
            marketing and operations teams one hyperlocal decision plane.
          </p>
        </div>
        <div className="hero-stats">
          <div className="metric panel">
            <span>Physical ROI Index</span>
            <strong>{overview.physical_roi_index}</strong>
          </div>
          <div className="metric panel">
            <span>Signal Health</span>
            <strong>{overview.signal_health_index}</strong>
          </div>
          <div className="metric panel accent">
            <span>Top Zone</span>
            <strong>{overview.top_zone.name}</strong>
          </div>
        </div>
      </section>

      <section className="grid">
        <article className="panel span-7">
          <div className="section-head">
            <h2>Hyperlocal Zone Board</h2>
            <p>Spatial priority scoring across physical demand clusters.</p>
          </div>
          <div className="zone-map">
            {zones.map((zone, index) => (
              <div className={`zone-card zone-${index % 4}`} key={zone.zone_id}>
                <div className="zone-meta">
                  <span>{zone.city}</span>
                  <strong>{zone.name}</strong>
                </div>
                <div className="zone-metrics">
                  <div>
                    <label>ROI</label>
                    <b>{zone.local_roi_score}</b>
                  </div>
                  <div>
                    <label>Pressure</label>
                    <b>{zone.pressure_score}</b>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </article>

        <article className="panel span-5">
          <div className="section-head">
            <h2>Field Action Queue</h2>
            <p>What the swarm wants your team to approve or escalate.</p>
          </div>
          <div className="action-list">
            {agents.map((agent) => (
              <div className="action-card" key={agent.agent}>
                <div className="action-top">
                  <h3>{agent.agent}</h3>
                  <span>{Math.round(agent.confidence * 100)}%</span>
                </div>
                <p>{agent.action}</p>
                <small>{agent.rationale}</small>
              </div>
            ))}
          </div>
        </article>

        <article className="panel span-6">
          <div className="section-head">
            <h2>Operating Thesis</h2>
            <p>The platform keeps physical marketing measurable and resilient.</p>
          </div>
          <div className="pillars">
            <div className="pillar">
              <strong>Sense</strong>
              <p>Fuse WiFi, satellite, event, and competitor signals into one local context layer.</p>
            </div>
            <div className="pillar">
              <strong>Interpret</strong>
              <p>Use agents to turn real-world context into actionable creative and budget guidance.</p>
            </div>
            <div className="pillar">
              <strong>Predict</strong>
              <p>Model lift and spillover before launching or scaling a hyperlocal campaign.</p>
            </div>
            <div className="pillar">
              <strong>Respect Privacy</strong>
              <p>Favor edge inference and aggregated signals instead of invasive identity tracking.</p>
            </div>
          </div>
        </article>

        <article className="panel span-6">
          <div className="section-head">
            <h2>Spatial Story</h2>
            <p>The memorable part of the product is that it thinks in places, not just audiences.</p>
          </div>
          <div className="story-card">
            <h3>{overview.top_zone.name}</h3>
            <p>
              Tonight’s strongest zone blends commuter density, social demand, and manageable competitor noise. The
              swarm favors timely, culturally aware creative over blunt radius targeting.
            </p>
          </div>
        </article>
      </section>
    </main>
  );
}

export default App;

