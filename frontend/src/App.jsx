import { useEffect, useState } from "react";
import { getCostSummary } from "./api";

export default function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    getCostSummary().then(setData);
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div style={{ maxWidth: 900, margin: "auto", padding: 20 }}>
      <h1>Cloud Cost Optimization Dashboard</h1>

      <h2>Total Monthly Cost: ${data.total_monthly_cost}</h2>
      <h3>Estimated Savings: ${data.estimated_monthly_savings}</h3>

      <h3>Cost by Service</h3>
      <ul>
        {data.cost_by_service.map(s => (
          <li key={s.service}>
            {s.service}: ${s.monthly_cost}
          </li>
        ))}
      </ul>

      <h3>Idle / Underutilized Resources</h3>
      <ul>
        {data.idle_resources.map(r => (
          <li key={r.resource_id}>
            {r.service} - {r.resource_id} (${r.monthly_cost})
          </li>
        ))}
      </ul>

      <h3>Recommendations</h3>
      <ul>
        {data.recommendations.map((r, i) => <li key={i}>{r}</li>)}
      </ul>
    </div>
  );
}
