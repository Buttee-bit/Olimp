from fastapi import APIRouter, Depends
import fastapi_users

from ..auth.models import User
from .schemas import UserRead,UserCreate
from .base_config import auth_backend, fastapi_users

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
def protected_lk(user: User = Depends(current_user)):
    return f'Hi: {user.email} you register at { user.register_at}' 