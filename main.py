from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

tasks = [
    {"id": 1, "title": "sweeping", "done": True},
    {"id": 2, "title": "washing", "done": False},
    {"id": 3, "title": "praying", "done": True}
]


@app.get("/")
def get_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}


@app.get("/health")
def check_health():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{id}")
def get_id_tasks(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {id} not found")
