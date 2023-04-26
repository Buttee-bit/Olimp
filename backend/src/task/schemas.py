from pydantic import BaseModel
from datetime import datetime


class OlimpiadCreate(BaseModel):
    title : str
    order : str
    # time_start : 
    # time_end : 
    # work_time : int


class Olimpiadraed(BaseModel):
    id : int
    title : str
    order : str
    time_start : datetime
    time_end : datetime
    work_time : int
