from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()


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


@app.get("/")
def get_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}


@app.get("/health")
def check_health():
    return {"status": "ok"}


@app.get("/tasks", description="Get a list of tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{id}", description="fetch a single task by its ID.")
def get_id_tasks(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {id} not found")


@app.post("/tasks", status_code=201, description="create a new task and add it to the existing list of tasks and return the task")
def create_task(new_task: TaskCreate):
    if new_task.title == "":
        raise HTTPException(status_code=400, detail="title is empty")

    next_id = tasks[-1]["id"] + 1 if tasks else 1
    task = {"id": next_id, "title": new_task.title, "done": False}
    tasks.append(task)
    return task


@app.put("/tasks/{id}", description="update a single task by its ID.")
def update_task(id: int, update: TaskUpdate):
    for task in tasks:
        if task["id"] == id:
            if update.title is not None:
                task["title"] = update.title
            if update.done is not None:
                task["done"] = update.done
            return task
    raise HTTPException(status_code=404, detail=f"Task {id} not found")


@app.delete("/tasks/{id}", status_code=204, description="delete a single task by its ID and this action is irreversible.")
def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return None
    raise HTTPException(status_code=404, detail="no match found")
