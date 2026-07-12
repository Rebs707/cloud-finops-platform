from fastapi import FastAPI
from app.api.finops import router as finops_router

app = FastAPI(
    title="Cloud FinOps Platform",
    version="1.0.0"
)

app.include_router(finops_router)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "platform": "Cloud FinOps Platform"
    }
