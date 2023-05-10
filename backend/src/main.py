from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .task.router import router as task_router
from .auth.router import router as auth_router
from .olimpiads.router import router as olimp_router 

app = FastAPI(
    title="Olimpiad App"
)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Content-Type","Set-Cookie"], 
)

app.include_router(task_router)
app.include_router(auth_router)
app.include_router(olimp_router)