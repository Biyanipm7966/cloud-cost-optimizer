from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mock_data import CLOUD_RESOURCES
from analyzer import analyze_cost

app = FastAPI(title="Cloud Cost Optimization API")

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # React dev server
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/cost-summary")
def cost_summary():
    return analyze_cost(CLOUD_RESOURCES)
