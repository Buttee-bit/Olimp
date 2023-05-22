import json
from fastapi import APIRouter, Depends
import fastapi_users
from sqlalchemy.ext.asyncio import AsyncSession
from ..auth.models import user
from ..database import get_async_session
from .schemas import UserRead, UserCreate
from .base_config import auth_backend, fastapi_users
from sqlalchemy import select
from fastapi.responses import JSONResponse
router = APIRouter(
    prefix = '/lk',
    tags = ['lk']
)


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),

)
current_user = fastapi_users.current_user()

@router.get('/personalCabinet')
async def protected_lk(user_pol: user = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    return JSONResponse(content={
        'name' : user_pol.name,
        'city' : user_pol.city,
        'class_' : user_pol.class_,
        'School' : user_pol.School
    })
