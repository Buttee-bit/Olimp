from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import olimpiad
from ..database import get_async_session
import fastapi_users
from ..auth.base_config import fastapi_users
from ..auth.models import User
from .models import task, olimpiad, modyle, decription, answer, user_answer
from ..olimpiads.schemas import OlimpRegister
# from .schemas import OlimpiadCreate

router = APIRouter(
    prefix = '/task',
    tags = ['task']
)

current_user = fastapi_users.current_user()


@router.get('/task/{id}')
async def protect_get_task_for_olimpiad(id:int, user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    # stmt = select(task).where(olimpiad.c.id == id_olimp)
    print(id)
    return {'id':id}
# @router.get()


# Перенести в олимпиады или админку !!!! 
# @router.post('/olimpiad') 
# async def post_olimpiad(new_olimpiad : OlimpiadCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(olimpiad).values(**new_olimpiad.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {
#         'olimpiad': 'succes created'
#     }