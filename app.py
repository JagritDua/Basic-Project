from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Hello Hello6"

@app.route("/testing2")
def home2():
    return "testing 2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
