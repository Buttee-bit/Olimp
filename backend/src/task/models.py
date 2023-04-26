from datetime import datetime,timedelta
from sqlalchemy import ForeignKey, MetaData, Table, Column, Integer, String, TIMESTAMP
from ..auth.models import user

metadata = MetaData()

olimpiad = Table(
    'olimpiad',
    metadata,
    Column("id", Integer, primary_key=True),
    Column('title', String),
    Column('order', String),
    Column("time_start", TIMESTAMP, default = datetime.utcnow),
    Column("time_end", TIMESTAMP, default = ((datetime.utcnow()) + timedelta(days=2))),
    Column("work_time", Integer, default = 7200)
)

modyle = Table(
    'module',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String)
)



decription = Table(
    'decriptions',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('text_decription', String)
)

type_task = Table(
    'type_task',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('text', String)
)
task = Table(
    'task', 
    metadata,
    Column("id", Integer, primary_key=True),
    Column("id_olimpiad", Integer, ForeignKey(olimpiad.c.id)),
    Column('title', String),
    Column('module', Integer, ForeignKey(modyle.c.id)),
    Column('decription', Integer, ForeignKey(decription.c.id)),
    Column('text', String),
    Column('type', Integer, ForeignKey(type_task.c.id)),
)

answer = Table(
    'answer',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('id_task', Integer, ForeignKey(task.c.id)),
    Column('text', String),
    Column('status', Integer)   
)

user_answer = Table(
    'user_answer', 
    metadata,
    Column('id', Integer, primary_key=True),
    Column('id_user', Integer, ForeignKey(user.c.id)), 
    Column('id_task', Integer, ForeignKey(task.c.id)),
    Column('id_answer', Integer, ForeignKey(answer.c.id)),
    Column('id_olimpiad', Integer, ForeignKey(olimpiad.c.id)),
    Column('score', Integer)
)

total_score = Table(
    'total_score', 
    metadata,
    Column('id', Integer, primary_key=True),
    Column('id_user', Integer, ForeignKey(user.c.id)), 
    Column('id_olimpiad', Integer, ForeignKey(olimpiad.c.id)),
    Column('total_score', Integer)
)


# files_task = Table(
#     'files_task',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name_file', String)
#     Column('path_file', String)
#     Column('')
# )