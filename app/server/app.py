from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.server.routes.env_problems import router as EnvProblemRouter
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(EnvProblemRouter, tags=["envProblems"], prefix="/envProblems")
app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
