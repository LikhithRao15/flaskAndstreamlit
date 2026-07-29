from flask import Flask, jsonify, request

app=Flask(__name__)
result=None

@app.route('/')
def home():
    return "Hello, Flask is working!"



@app.route('/add', methods=['POST'])
def add():
    global result
    data=request.get_json()
    num1=data['num1']
    num2=data['num2']
    result=num1+num2
    return jsonify({"result":result})

@app.route('/add', methods=['GET'])
def get_add():
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)