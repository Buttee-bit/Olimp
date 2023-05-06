from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .auth.base_config import auth_backend, fastapi_users
from .auth.schemas import UserRead, UserCreate
from .task.router import router as task_router
# from operations.router import router as router_operation

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
    allow_headers=["Content-Type","Set-Cookie"], # include additional headers as per the application demand
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(task_router)
