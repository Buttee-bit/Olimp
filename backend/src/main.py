from fastapi import FastAPI

from .auth.base_config import auth_backend, fastapi_users
from .auth.schemas import UserRead, UserCreate
from .task.router import router as task_router
# from operations.router import router as router_operation

app = FastAPI(
    title="Olimpiad App"
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