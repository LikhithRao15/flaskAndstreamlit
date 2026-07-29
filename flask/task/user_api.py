from flask import Flask, jsonify

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is working!"

@app.route('/hello/<username>',methods=['GET'])
def hello(username):
    return jsonify({"message":f"hello {username} from API"})

if __name__ == '__main__':
    app.run(debug=True)