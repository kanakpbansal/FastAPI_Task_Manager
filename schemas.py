#Pydantic models (request/response)
from pydantic import BaseModel
from typing import Optional

class Tasks(BaseModel):
    id:Optional[int]
    title:str
    description:str
    completed:bool=False
    deadline:Optional[str]=None
    class Config():
        orm_mode=True

    