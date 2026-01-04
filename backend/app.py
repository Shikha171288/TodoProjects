from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary storage (in-memory)
tasks = []
task_id = 1

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Create a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    global task_id
    data = request.json

    task = {
        "id": task_id,
        "title": data["title"],
        "completed": False
    }

    tasks.append(task)
    task_id += 1
    return jsonify(task), 201

# Update task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    for task in tasks:
        if task["id"] == id:
            task["completed"] = not task["completed"]
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# Delete task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
