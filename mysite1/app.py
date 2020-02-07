from flask import Flask
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/")
def index():
    return "<h1>Hello World</h1>"

# http://127.0.0.1:5000/hi
@app.route("/hi")
def hi():    
    return "Hi World"

if __name__ == "__main__":
    app.run()