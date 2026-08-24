Dependencies to install
pip install -r requiremnt.txt

To start server
```bash
uvicorn main:app --reload
```

URL to run
run http://127.0.0.1:8000/docs in your browser

| Method | Path | Description |
|--------|------|-------------|
| GET | / | Root endpoint, basic welcome/status message |
| GET | /health | Check if the server is running |
| GET | /tasks | Fetch the full list of tasks |
| GET | /tasks/{id} | Fetch a single task by its ID |
| POST | /tasks | Create a new task and add it to the list |
| PUT | /tasks/{id} | Update an existing task by its ID |
| DELETE | /tasks/{id} | Permanently delete a task by its ID |

curl.exe -g -i -X POST "http://127.0.0.1:8000/tasks" -H "Content-Type: application/json" -d "@body.json"

![Swagger UI screenshot](screenshot/swagger.png)