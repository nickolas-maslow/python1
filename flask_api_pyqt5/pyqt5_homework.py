import requests
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

response = requests.get(url='http://127.0.0.1:5000/')


def application():
    app = QApplication(sys.argv)
    window = QMainWindow

    window.setWindowTitle("Flask output")
    window.setGeometry(300, 250, 350, 200)

    main_text = QtWidgets.QLabel(window)
    main_text.setText(response)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()

