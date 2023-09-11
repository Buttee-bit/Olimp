from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
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

@router.get('/timer_olimp/{id_olimp}')
async def protect_get_time_olimpiad(id_olimp:int,user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    timer_stmt  = select(olimpiad).where(olimpiad.c.id == id_olimp)
    timer_res = await session.execute(timer_stmt)
    data_timer = timer_res.fetchone()
    list_data = []
    print(data_timer)
    list_data.append({
        'time':data_timer[-1]
    })
    return JSONResponse(content=list_data)


@router.get('/olimp/{id_olimp}/task/{id_task}')
async def protect_get_task_for_olimpiad(id_olimp:int,id_task:int, user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    # stmt = select(task).where(olimpiad.c.id == id_olimp)
    olimpiad_stmt = select(olimpiad).where(olimpiad.c.id == id_olimp)
    olimpiad_res = await session.execute(olimpiad_stmt)
    data_olimp_res = olimpiad_res.fetchone()
    print(data_olimp_res[1]) #title olimp

    question_stmt = select(task).where(task.c.id_olimpiad == id_olimp).where(task.c.id == id_task)
    question_res = await session.execute(question_stmt)
    data_question_res = question_res.fetchone()
    print(data_question_res)
    # print(data_question_res[2],data_question_res[-2])#title task, text task


    if data_question_res[-1] == 3:
        pass
    else:
        decription_stmt = select(decription).where(decription.c.id == data_question_res[0])
        decription_res = await session.execute(decription_stmt)
        data_decription = decription_res.fetchone()
        print(data_decription[1]) # decription text

        answer_stmt = select(answer).where(answer.c.id_task == data_question_res[0])
        answer_res = await session.execute(answer_stmt)
        data_answer = answer_res.fetchall()
        print(data_answer) # answers

    data = [{
        'id_olimp': data_olimp_res[0],
        'id_task': data_question_res[0],
        'type_task': data_question_res[-1],
        'olimp_title': data_olimp_res[1],
        'number_task': 1,
        'title_task': data_question_res[2],
        'score_task': 1,
        'text_task': data_question_res[-2],
        'decription_task': data_decription[1],
    }]
    return JSONResponse(content=data)
    # id_olimp
    # id_task
    # type_task
    # olimp_title
    # number_task
    # title_task
    # score_task
    # text_task
    # decription_task
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