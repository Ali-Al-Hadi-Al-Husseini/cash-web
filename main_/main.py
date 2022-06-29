from flask import Flask


app = Flask(__name__)


@app.route("/")
def main():
    return "HOLA MI AMIGO"


if __name__ == "__main__":
    app.run(debug=True)
    