from flask import Flask, jsonify, request

app=Flask(__name__)

users=[]

@app.route('/')
def home():
    return "Hello, Flask is working!"

@app.route('/hello')
def hello():
    return jsonify({"message":"hello World from API"})

@app.route('/users',methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users',methods=['POST'])
def add_user():
    data=request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error":"Please provide name and email"}), 400
    users.append({"name":data['name'],"email":data['email']})
    return jsonify({"message":"User added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)


