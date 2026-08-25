from connected import conn


def create_table():
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS tasks (id integer primary key, title text, done boolean)")
    conn.commit()


def get_all_tasks():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    return rows


def get_task_by_id(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
    row = cursor.fetchone()
    return row


def create_task(title, done):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)", (title, done))
    conn.commit()
    return cursor.lastrowid


def update_task(id, task, done):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET (id, tasks, done) WHERE id = ?", (id, task, done))
    conn.commit()


def delete_tasks(id):
    cursor = conn.cursor()
    cursor.execute("DELETE from tasks WHERE id = ?", (id,))
    conn.commit()
