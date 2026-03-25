from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store
users = {}
tasks = {}

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    uid = len(users) + 1
    users[uid] = {"id": uid, "name": data["name"], "email": data["email"]}
    return jsonify(users[uid]), 201

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(list(tasks.values()))

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    tid = len(tasks) + 1
    tasks[tid] = {"id": tid, "title": data["title"], "done": False}
    return jsonify(tasks[tid]), 201

if __name__ == "__main__":
    app.run(debug=True)
