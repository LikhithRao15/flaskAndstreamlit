from flask import Flask, jsonify, request
app=Flask(__name__)
todos=[]
@app.route('/')
def home():
    return "Hello, Flask is working!"

@app.route('/todo', methods=['POST'])
def add_todo():
    data=request.get_json()
    todo=data['todo']
    todos.append(todo)
    return jsonify({"message":"Todo added successfully!"}),201

@app.route('/todo', methods=['GET'])
def get_todos():
    return jsonify(todos)

if __name__ == '__main__':
    app.run(debug=True)
