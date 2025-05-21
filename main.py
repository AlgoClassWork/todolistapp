from flask import Flask, render_template, request, redirect
from database import *

app = Flask(__name__)

#http://127.0.0.1:5000/
@app.route('/')
def main_page():
    tasks = get_all_tasks() 
    return render_template('index.html', tasks=tasks)

#http://127.0.0.1:5000/add
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    return redirect('/')

app.run()
