import pandas as pd

def analyze_cost(resources):
    df = pd.DataFrame(resources)

    total_cost = df["monthly_cost"].sum()

    cost_by_service = (
        df.groupby("service")["monthly_cost"]
        .sum()
        .reset_index()
        .to_dict(orient="records")
    )

    idle_resources = []

    for r in resources:
        if r["service"] == "EC2" and r.get("avg_cpu_util", 100) < 5:
            idle_resources.append(r)
        if r["service"] == "EBS" and r.get("attached") is False:
            idle_resources.append(r)
        if r["service"] == "S3" and r.get("access_freq") == "low":
            idle_resources.append(r)

    estimated_savings = sum(r["monthly_cost"] for r in idle_resources)

    recommendations = [
        f"Terminate or downsize {len(idle_resources)} underutilized resources"
        if idle_resources else "No major idle resources detected"
    ]

    return {
        "total_monthly_cost": round(total_cost, 2),
        "cost_by_service": cost_by_service,
        "idle_resources": idle_resources,
        "estimated_monthly_savings": round(estimated_savings, 2),
        "recommendations": recommendations
    }
