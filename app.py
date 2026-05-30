from flask import Flask

from flask import render_template

app = Flask(__name__)

student = ["Anna", "Bob", "Charlie", "David", "Eva"]


@app.route("/")
def hello_world():
    return render_template("home.html", person=student)



# pip install flask
# flask run --port 8000 --debug
# flask run --port 8000 --debug