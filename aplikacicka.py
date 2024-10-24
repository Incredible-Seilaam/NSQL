from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")

@app.route("/library")
def bla():
    return render_template("library.html")

if __name__ == "__main__":
    app.run(debug=True)