from fastapi import APIRouter, Depends
import fastapi_users
from ..auth.base_config import fastapi_users

from ..task.models import olimpiad
current_user = fastapi_users.current_user()



router = APIRouter(
    prefix = '/olimpiads',
    tags = ['olimpiads']
)
# current_user = fastapi_users.current_user()
# @router.get('/')
# async def get_task(user: User = Depends(current_user)):

#     return f'hello', {user.email}