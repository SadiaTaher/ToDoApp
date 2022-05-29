from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

''' #single quote
__authors__ = ['Sadia Taher']
__date__ = 05_26_2022
__description__ = 'To-DO application for CICD'
'''

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):                           
    """A dummy docstring."""
    id = db.Column(db.Integer, primary_key=True)   # I am creating a variable "id". I want to tha variable to initiate the database. It initialize a colum of my table/databas. The function db.colum() takes arguments or parameters.
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/")
def list1():     
    """A dummy docstring."""
    todo_list = Todo.query.all() 
    return render_template("list.html", todo_list=todo_list)


@app.route("/edit")
def home():
    """A dummy docstring."""
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    """A dummy docstring."""
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    """A dummy docstring."""
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    """A dummy docstring."""
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    db.create_all()
    app.run()













