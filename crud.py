# Database operations
from fastapi import Depends,HTTPException,FastAPI
from database import get_db
from models import Task
from schemas import Tasks
from sqlalchemy.orm import Session

app=FastAPI()
@app.post("/task")
def create_task(t:Tasks,db:Session=Depends(get_db)):
    task = Task(**t.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return {"msg":"Task created"}

@app.get("/tasks/{task_id}")
def read_task(task_id:int,db:Session=Depends(get_db)):
    id=db.query(Task).filter(Task.id==task_id).first()
    if not id:
      raise HTTPException(status_code=404,detail="Task not found")
    return id

@app.patch("/tasks/{task_id}/update")
def update_task(task_id:int,t:Tasks,db:Session=Depends(get_db)):
    id=db.query(Task).filter(Task.id==task_id).first()
    if not id:
        raise HTTPException(status_code=404,detail="Task not found")
    id.title=t.title
    id.description=t.description
    id.completed=t.completed
    id.deadline=t.deadline
    db.commit()
    return {"msg":"Task updated"}

@app.delete("/tasks/{task_id}/delete")
def delete_task(task_id:int,db:Session=Depends(get_db)):
    id=db.query(Task).filter(Task.id==task_id).first()
    if not id:
        raise HTTPException(status_code=404,detail="Task not found")
    db.delete(id)
    db.commit()
    return {"msg":"Task deleted"}