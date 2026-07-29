from flask import Flask,jsonify

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is working!"

@app.route('/hello')
def hello():
    return jsonify({"message":"hello World from API"})

if __name__ == '__main__':
    app.run(debug=True)
    