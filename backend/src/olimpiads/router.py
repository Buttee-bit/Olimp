import datetime
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

import fastapi_users

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session
from ..auth.base_config import fastapi_users

from ..auth.models import User
from .models import olimpiad, users_in_olimpiad
from .schemas import OlimpRegister

current_user = fastapi_users.current_user()



router = APIRouter(
    prefix = '/olimpiads',
    tags = ['olimpiads']
)
current_user = fastapi_users.current_user()
@router.get('/all/not_end')
async def protected_get_olimpiads_not_end(user: User = Depends(current_user) ,session: AsyncSession = Depends(get_async_session)):
    stmt = select(olimpiad).where(olimpiad.c.time_end > datetime.datetime.utcnow())
    res = await session.execute(stmt)
    data = res.fetchall()
    list_data = []
    for olimpiad_ in data:
        print(olimpiad_[0])
        list_data.append({
            'id_olimp':olimpiad_[0],
            'title':olimpiad_[1],
            'time_end_data':olimpiad_[4].strftime("%d.%m.%Y"),
            'time_end_hours':olimpiad_[4].strftime("%H:%M"),
        })
    return JSONResponse(content=list_data)

@router.get('/all/end')
async def protect_get_olimpiads_end(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    stmt = select(olimpiad).where(olimpiad.c.time_end < datetime.datetime.utcnow())
    res = await session.execute(stmt)
    data = res.fetchall()
    list_data = []
    for olimpiad_ in data:
        list_data.append({
            'id_olimp':olimpiad_[0],
            'title':olimpiad_[1],
            'time_end_data':olimpiad_[4].strftime("%d.%m.%Y"),
            'time_end_hours':olimpiad_[4].strftime("%H:%M"),
        })
    return JSONResponse(content=list_data)

@router.post('/register/olimpiad')
async def protect_register_olimpiad(id_olimp:OlimpRegister,user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    stmt = select(olimpiad).where(olimpiad.c.id == id_olimp.id) # Передал через vue id олимпиады
    res = await session.execute(stmt)
    data = res.fetchall()
    print(data)
