from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from connected import conn

from crud import (
    create_table,
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_tasks
)
app = FastAPI()

create_table()


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str = None
    done: bool = None


tasks = [
    {"id": 1, "title": "sweeping", "done": True},
    {"id": 2, "title": "washing", "done": False},
    {"id": 3, "title": "praying", "done": True}
]


def row_to_dict(row):
    return dict(row)


@app.get("/")
def get_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}


@app.get("/health")
def check_health():
    return {"status": "ok"}


@app.get("/tasks", description="Get a list of tasks")
def get_tasks():
    rows = get_all_tasks()
    return [row_to_dict(row) for row in rows]


@app.get("/tasks/{id}", description="fetch a single task by its ID.")
def get_id_tasks(id: int):
    row = get_task_by_id(id)
    if row is None:
        raise HTTPException(status_code=404, detail=f"Task {id} not found")
    return row_to_dict(row)


@app.post("/tasks", status_code=201, description="Create a new task and return it.")
def create_task_route(new_task: TaskCreate):
    if new_task.title == "":
        raise HTTPException(status_code=400, detail="title is empty")

    new_id = create_task(new_task.title, False)
    row = get_task_by_id(new_id)
    return row_to_dict(row)


@app.put("/tasks/{id}", description="update a single task by its ID.")
def update_task(id: int, update: TaskUpdate):
    row = get_task_by_id(id)
    if row is None:
        raise HTTPException(status_code=404, detail=f"Task {id} not found")
    update_task(id, update.title, update.done)
    updated_row = get_task_by_id(id)
    return row_to_dict(updated_row)


@app.delete("/tasks/{id}", status_code=204, description="delete a single task by its ID and this action is irreversible.")
def delete_task(id: int):
    row = get_task_by_id(id)
    if row is None:
        raise HTTPException(status_code=404, detail="no match found")
    delete_tasks(id)
