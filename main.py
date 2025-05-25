from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)

#http://127.0.0.1:5000/
@app.route('/')
def main_page():
    tasks = database.get_all_tasks() 
    return render_template('index.html', tasks=tasks)

#http://127.0.0.1:5000/add
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    database.add_task(title, description)
    return redirect('/')

#http://127.0.0.1:5000/delete/1
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    database.delete_task(task_id)
    return redirect('/')

database.init_database()
app.run()
