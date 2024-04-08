from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Marcellino Halim - 2602201315!"

@app.route("/home")
def home():
    return "Hello, this is HOME page!"

@app.route("/profile")
def profile():
    return "Hello, this is PROFILE page!"

if __name__ == "__main__":
    app.run(port=int("3000"), debug=True)