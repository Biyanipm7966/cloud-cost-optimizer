# Simulated AWS usage & cost data (monthly)

CLOUD_RESOURCES = [
    {
        "service": "EC2",
        "resource_id": "i-01",
        "monthly_cost": 120.0,
        "avg_cpu_util": 3.2,
        "state": "running"
    },
    {
        "service": "EC2",
        "resource_id": "i-02",
        "monthly_cost": 85.0,
        "avg_cpu_util": 1.1,
        "state": "running"
    },
    {
        "service": "EBS",
        "resource_id": "vol-01",
        "monthly_cost": 40.0,
        "attached": False
    },
    {
        "service": "S3",
        "resource_id": "bucket-logs",
        "monthly_cost": 22.5,
        "storage_gb": 850,
        "access_freq": "low"
    },
    {
        "service": "RDS",
        "resource_id": "db-prod",
        "monthly_cost": 260.0,
        "avg_cpu_util": 12.0
    }
]
