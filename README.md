# Cloud Cost Optimizer

A web application that analyzes AWS cloud infrastructure costs, detects idle or underutilized resources, and provides actionable recommendations to reduce cloud spending.

## Features

- **Cost Dashboard** — Total monthly spend at a glance
- **Service Breakdown** — Costs grouped by AWS service (EC2, EBS, S3, RDS, etc.)
- **Idle Resource Detection** — Flags underutilized resources:
  - EC2 instances with CPU utilization < 5%
  - Unattached EBS volumes
  - S3 buckets with low access frequency
- **Savings Estimate** — Calculates potential monthly savings from removing idle resources
- **Recommendations** — Actionable suggestions for each detected issue

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 19, Vite 7 |
| Backend | FastAPI, Uvicorn |
| Data Analysis | Pandas |
| Communication | REST API (JSON) |

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --port 8010
```

API available at `http://localhost:8010/api/cost-summary`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

App available at `http://localhost:5173`

## Project Structure

```
cloud-cost-optimizer/
├── backend/
│   ├── main.py          # FastAPI app and API routes
│   ├── analyzer.py      # Cost analysis and idle resource detection
│   ├── mock_data.py     # Sample AWS resource data
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── App.jsx      # Main dashboard component
    │   ├── api.js       # Backend API client
    │   └── main.jsx     # Entry point
    └── package.json
```

## How It Works

1. The backend loads mock AWS resource data and runs it through the analyzer
2. The analyzer groups costs by service, applies utilization thresholds, and generates recommendations
3. The frontend fetches the summary from `/api/cost-summary` and renders the dashboard

## Development Notes

The app currently uses mock data in `backend/mock_data.py`. To connect real AWS data, replace the mock resources with calls to the AWS SDK (boto3) and feed the results into the existing analyzer logic.
