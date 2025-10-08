#FASTAPI app
import uvicorn
from crud import app

if __name__ == "__main__":
    uvicorn.run("crud:app", host="127.0.0.1", port=8000, reload=True)
