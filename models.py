#SQLAlchemy Models(Tables)
from database import Base,engine
from sqlalchemy import Column,String,Integer,Boolean

class Task(Base):
    __tablename__="tasks"
    id=Column(Integer(),primary_key=True,index=True)
    title=Column(String(100),nullable=False)
    description=Column(String(300),nullable=False)
    completed=Column(Boolean(),default=False,nullable=False)
    deadline=Column(String(50),nullable=True)

Base.metadata.create_all(engine)