from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    db.close()
    return render_template("index.html", tareas=tareas)

@app.route("/agregar", methods=["POST"])
def agregar():
    tarea = request.form["tarea"]
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO tareas (descripcion) VALUES (?)", (tarea,))
    db.commit()
    db.close()
    return redirect("/")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
    db.commit()
    db.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
