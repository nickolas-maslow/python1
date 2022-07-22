from flask import Flask
from logic import fine_text

app = Flask(__name__)


@app.route('/')
def homepage():
    """читаем текстовый файл в большую строку"""

    return fine_text


if __name__ == '__main__':
    app.run(debug=True)