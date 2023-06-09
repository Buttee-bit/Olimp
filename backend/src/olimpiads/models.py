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

users_in_olimpiad = Table(
    'users_in_olimpiad',
    metadata,
    Column("id", Integer, primary_key=True),
    Column('id_olimpiad', Integer, ForeignKey(olimpiad.c.id)),
    Column('user_id', Integer, ForeignKey(user.c.id))
)
