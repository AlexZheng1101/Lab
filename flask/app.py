from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///box.db'

db = SQLAlchemy(app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    content = db.Column(db.String(200), nullable = False)
    people = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
def __repr__(self):
    return '<task %r>' % self.id
@app.route("/", methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        task_title = request.form["title"]
        task_content = request.form["content"]
        task_people = request.form["people"]
        data = Todo(title=task_title, content=task_content, people=task_people)
        try:
            db.session.add(data)
            db.session.commit()
            return redirect("/")
        except:
            return "Fail To Add New Issue To Your task."
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('home.html', tasks=tasks) #沒有POST新任務的話，就顯示目前資料中的任務
        
@app.route("/delete/<int:id>")

def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "deleteing Problem."

@app.route("/update/<int:id>", methods=['POST', 'GET'])

def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.title = request.form['title']
        task.content = request.form['content']
        task.people = request.form['people']
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "Updating Issue."
    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=1000)