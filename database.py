import sqlite3

def get_connection():
    connection = sqlite3.connect('todo_list.db')
    connection.row_factory = sqlite3.Row
    return connection

def init_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    done INTEGER DEFAULT 0) ''')
    connection.commit()
    connection.close()

def add_task(title, description=''):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO tasks (title, description)
    VALUES (?, ?)''', (title, description))
    connection.commit()
    connection.close()

def delete_task(task_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    connection.commit()
    connection.close()

def update_task(task_id, title, description, done):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(''' UPDATE tasks SET title =?, description =?, done=?
                       WHERE id =?''', (title, description, done, task_id))
    connection.commit()
    connection.close()

def task_done(task_id):
    task = get_task(task_id)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE tasks SET done = ? WHERE id = ?',
                   (0 if task['done'] else 1, task_id)    )
    connection.commit()
    connection.close()

def get_task(task_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    connection.close()
    return task

def get_all_tasks():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    connection.close()
    return tasks