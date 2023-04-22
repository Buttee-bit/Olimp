import datetime 
from sqlalchemy import MetaData, Table, JSON,ForeignKey, Column, Integer, String, TIMESTAMP

metadata = MetaData()

roles = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, primary_key=False),
    Column('permissions', JSON),

)

user = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('city', String),
    Column('class', Integer),
    Column('School', String),
    Column('register_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey("roles.id")),

)