from flask import Flask, jsonify

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
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

