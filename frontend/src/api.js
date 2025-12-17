export async function getCostSummary() {
    const res = await fetch("http://localhost:8010/api/cost-summary");
    return res.json();
  }
  