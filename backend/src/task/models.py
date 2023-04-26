from datetime import datetime
from sqlalchemy import  MetaData, Table, Column, Integer, String, TIMESTAMP
metadata = MetaData()

task = Table(
    'task', 
    metadata,
    Column("id", Integer, primary_key=True),
    Column("id_olimpiad", Integer),
    Column('title', String),
    Column('module', Integer),
    Column('text', String),
    Column('type', Integer),
    Column('description_id',Integer)
)

olimpiad = Table(
    'olimpiad',
    metadata,
    Column("id", Integer, primary_key=True),
    Column('title', String),
    Column("time_start", TIMESTAMP, default = datetime.utcnow),
    Column("time_end", TIMESTAMP, default = datetime.utcnow),
    Column("work_time", Integer, default = 7200 )
)

modyle = Table(
    'module',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String)
)

answer = Table(
    'answer',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('id_task', Integer),
    Column('text', String),
    Column('status', Integer)   
)
