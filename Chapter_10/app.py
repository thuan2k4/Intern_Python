from flask import Flask, render_template, redirect, url_for, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
api = Api(app)

#Routes
@app.route("/")
def index():
    return render_template("index.html", tasks=Todo.query.all())

#Models
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    complete = db.Column(db.String(10), default="danger")
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "complete": self.complete
        }
    def __repr__(self):
        return f"<Todo {self.title}>"

#API
class TodoAPI(Resource):
    def get(self, todo_id):
        obj = Todo.query.filter_by(id=todo_id).first()
        if obj:
            return obj.to_dict()
        else:
            return {"error": "Task not found"}, 404
            
    def post(self, todo_id=None):
        if todo_id is None:
            data = request.form
            obj = Todo(title=data["title"], description=data["description"])
            db.session.add(obj)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            method = request.form.get('_method', '').upper()
            if method == 'PUT':
                return self.put(todo_id)
            elif method == 'DELETE':
                return self.delete(todo_id)
            return {"error": "Invalid method"}, 400
            
    def put(self, todo_id):
        data = request.form
        obj = Todo.query.filter_by(id=todo_id).first()
        if obj:
            obj.title = data["title"]
            obj.description = data["description"]
            obj.complete = data["complete"]
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return {"error": "Task not found"}, 404
            
    def delete(self, todo_id):
        obj = Todo.query.filter_by(id=todo_id).first()
        if obj:
            db.session.delete(obj)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return {"error": "Task not found"}, 404

#Register API
api.add_resource(TodoAPI, "/api/todo", methods=["POST"], endpoint="Create") 
api.add_resource(TodoAPI, "/api/todo/<int:todo_id>", methods=["GET", "POST"], endpoint="Read-Update-Delete")


#create db
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host=os.getenv("HOST"), port=os.getenv("PORT"))

#update no reload