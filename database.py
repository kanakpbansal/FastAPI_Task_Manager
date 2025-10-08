#Engine,Session,Base
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import os

Base=declarative_base()

base_dir=os.path.dirname(os.path.realpath(__file__))
connecting_string="sqlite:///"+os.path.join(base_dir,"task.db")
engine=create_engine(connecting_string,echo=True,connect_args={"check_same_thread": False})
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()