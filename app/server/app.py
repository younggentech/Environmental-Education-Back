from fastapi import FastAPI
from app.server.routes.env_problems import router as EnvProblemRouter
app = FastAPI()
app.include_router(EnvProblemRouter, tags=["envProblems"], prefix="/envProblems")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}