from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK"
tasks = [
{"id": 1, "title": "Learn Flask"},
    {"id": 2, "title": "Learn Docker"}
]

@app.route("/tasks")
def task():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def append_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"]
    }

    tasks.append(new_task)

    return jsonify(new_task), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

