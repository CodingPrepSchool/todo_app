from re import template
from flask import Flask, redirect, render_template, request
import sqlite3
from todo_app.forms import NewTask, DeleteTask

app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route("/")
def homepage():
    return render_template("index_todo.html")

@app.route("/todo-data/view-list")
def tdl():
    con = sqlite3.connect("tasks.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT tasks.completed, tasks.name, roommates.name AS roommates_name, tasks.date FROM roommates JOIN tasks ON tasks.user_id = roommates.user_id")
    rows = cur.fetchall()
    con.commit()
    con.close
    return render_template("to_do_list.html", rows=rows)

@app.route("/todo-data/add-task", methods=["GET", "POST"])
def add_task():
    new_task= NewTask(csrf_enabled = False)
    return render_template("add_task.html", template_form = new_task)

@app.route("/add_info", methods=["GET", "POST"])
def add_info():
    new_task = NewTask(csrf_enabled = False)
    if request.method == 'POST':
        con = sqlite3.connect("tasks.db")
        name = request.form['name']
        user_id = request.form['user_id']
        date = request.form['date']
        con.execute("INSERT INTO tasks (name, user_id, date) VALUES (?, ?, ?)", (name, user_id, date))
        con.commit()
        con.close
    return render_template('message.html', template_form = new_task)

@app.route("/todo-data/remove-task", methods=["GET", "POST"])
def delete_record():
    delete_task= DeleteTask(csrf_enabled = False)
    return render_template("delete_task.html", template_form = delete_task)


@app.route("/delete-info", methods=["GET", "POST"])
def delete_info():
    delete_task= DeleteTask(csrf_enabled = False)
    if request.method == 'POST':
        con = sqlite3.connect("tasks.db")
        name = request.form['name']
        con.execute("DELETE FROM tasks WHERE name = ?", [name])
        con.commit()
        con.close()
    return render_template('message_2.html', template_form = delete_task)

@app.route("/completed_task", methods=["GET", "POST"])
def completed():
    if request.method == 'POST':
        con = sqlite3.connect("tasks.db")
        completed = request.form['completed_value']
        task_id = request.form['task_id']
        con.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))
        con.commit()
        con.close()
    return redirect("/todo-data/view-list")