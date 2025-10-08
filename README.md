# FastAPI Task Manager
This is a simple task manager API built using **FastAPI** and **SQLAlchemy** with **SQLite**.
## Features
- Create tasks  
- Read tasks  
- Update tasks 
- Delete tasks 
- Track completion status  
- Optional deadlines
## Setup
1. Create and activate the virtual environment
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Mac/Linux
   ``` 
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn crud:app --reload
   ```
## API Endpoints
POST /task 
- Create a new task
   Example body:
   {
	"title": "Buy groceries",
 	"description": "Milk, Eggs, Bread",
  	"completed": false,
 	"deadline": "2025-10-15"
  }
2. GET /tasks/{task_id} 
   - Read a task by its ID
3. PUT /tasks/{task_id} 
   - Update a task by its ID
4. DELETE /tasks/{task_id}
   - Deletes a task by its ID
## Notes
  - Database used is SQLite (task.db)
  - Pydantic models handle request validation
  - SQLAlchemy handles ORM operations


