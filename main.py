from flask import Flask
from flask import render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum-secret-key'


@app.route("/")
@app.route("/home")
def home_index():
    return render_template("home_index.html")


def main():
    app.run(host="127.0.0.1", port=5050)


if __name__ == '__main__':
    main()
