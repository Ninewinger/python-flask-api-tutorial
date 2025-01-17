from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
  return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
  request_body = request.data
  todo_py = json.loads(request_body)
  todos.append(todo_py)
  return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)