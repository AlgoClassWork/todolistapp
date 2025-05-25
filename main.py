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
    if title:
        database.add_task(title, description)
    return redirect('/')

#http://127.0.0.1:5000/delete/1
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    database.delete_task(task_id)
    return redirect('/')

#http://127.0.0.1:5000/edit/8
@app.route('/edit/<int:task_id>', methods=['GET','POST'])
def edit_task(task_id):
    if request.method == 'GET':
        task = database.get_task(task_id)
        return render_template('edit.html', task=task)
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        done = 'done' in request.form
        database.update_task(task_id, title, description, done)
        return redirect('/')
    
#http://127.0.0.1:5000/done/2
@app.route('/done/<int:task_id>')
def task_done(task_id):
    database.task_done(task_id)
    return redirect('/')

database.init_database()
app.run()
