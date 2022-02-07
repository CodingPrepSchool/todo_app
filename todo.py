from flask import Flask,render_template,request,redirect
import sqlite3
from forms import ToDo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route("/")
def indexpage():
    return render_template("index_page.html")


@app.route("/todo/list")
def all_tasks():
    con = sqlite3.connect("todo.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT tasks.completed,tasks.task_name,roommates.roommate_name,tasks.due_date FROM tasks JOIN roommates ON tasks.task_id=rommates.task_id")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return render_template("roommates.html",rows = rows)


@app.route("/todo/add")
def new_task():
    new_task = ToDo(csrf_enabled=False)
    return render_template("add_new_task.html",template_form=new_task)

@app.route("/todo/added", methods=["GET","POST"])
def add_new_task():
    new_task = ToDo(csrf_enabled=False)
    if request.method == "POST":
        con = sqlite3.connect("todo.db")
        task_name = request.form["task_name"]
        roommate_name = request.form["asined_to"]
        due_by = request.form["due_by"]
        con.execute("INSERT INTO tasks (task_name,rommate_id,due_date) VALUES (?,?,?)", (task_name,roommate_name,due_by))
        con.commit()
        con.close()
    return render_template("message.html",template_form=new_task)

@app.route("/todo/delete")
def delete_tasks():
    del_task = ToDo(csrf_enabled=False)
    return render_template("delete_task.html",template_form=del_task)

@app.route("/delete-info-tasks", methods=["GET","POST"])
def delete_task():
    del_task = ToDo(csrf_enabled=False)
    if request.method == "POST":
        con = sqlite3.connect("todo.db")
        task_name = request.form["task_name"]
        con.execute("DELETE FROM tasks WHERE task_name = ?", [task_name])
        con.commit()
        con.close
    return render_template("message2.html",template_form=del_task)

@app.route("/complete_task", methods=["GET","POST"])
def checkbox():
    if request.method == "POST":
        con = sqlite3.connect("todo.db")
        task_id = request.form["task_id"]
        completed_value = request.form["completed_value"]
        con.execute("UPDATE tasks SET completed = ? WHERE task_id = ?", (completed_value,task_id))
        con.commit()
        con.close()
    return redirect("/todo/list")