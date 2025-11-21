from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import auth, strategies, backtests

app = FastAPI(
    title="AlgoTrader Pro API",
    description="Algorithmic Trading Backtesting Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(strategies.router, prefix="/api/v1/strategies", tags=["strategies"])
app.include_router(backtests.router, prefix="/api/v1/backtests", tags=["backtests"])

@app.get("/")
def root():
    return {"message": "AlgoTrader Pro API", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
