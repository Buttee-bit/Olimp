from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import olimpiad
from ..database import get_async_session
from .schemas import OlimpiadCreate

router = APIRouter(
    prefix = '/task',
    tags = ['task']
)


@router.get('/')
async def get_task(session: AsyncSession = Depends(get_async_session)):

    return 'hello'

@router.post('/olimpiad')
async def post_olimpiad(new_olimpiad : OlimpiadCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(olimpiad).values(**new_olimpiad.dict())
    await session.execute(stmt)
    await session.commit()
    return {
        'olimpiad': 'succes created'
    }