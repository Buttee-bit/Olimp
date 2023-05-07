# from fastapi import APIRouter, Depends
# import fastapi_users

# from ..auth.models import User



# router = APIRouter(
#     prefix = '/lk',
#     tags = ['lk']
# )
# current_user = fastapi_users.current_user()
# @router.get('/')
# async def get_task(user: User = Depends(current_user)):

#     return f'hello', {user.email}