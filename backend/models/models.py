import datetime 
from sqlalchemy import Boolean, MetaData, Sequence, Table, JSON,ForeignKey, Column, Integer, String, DateTime

metadata = MetaData()

role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('permissions', JSON),

)

user = Table(
    'user',
    metadata,
    Column("id", Integer, primary_key=True),
    Column('name', String),
    Column('email', String),
    Column('hashed_pass', String),
    Column('city', String),
    Column('class_', Integer),
    Column('School', String),
    Column('register_at', DateTime, default=datetime.datetime.utcnow),
    Column('role_id', Integer, ForeignKey("role.id")),
    Column('is_active',Boolean, default=True, nullable=False),
    Column('is_superuser',Boolean, default=False, nullable=False),
    Column('is_verified',Boolean, default=False, nullable=False)

)