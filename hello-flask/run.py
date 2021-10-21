from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello World!'


@app.route("/number/<num>")
def number(num):
    return 'Hello World! {}'.format(num)


if __name__ == "__main__":
    app.run(debug=True)
