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

#http://127.0.0.1:5000/del/3


database.init_database()
app.run()
