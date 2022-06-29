import sys
from threading import Thread

import requests
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QApplication
from bs4 import BeautifulSoup

url = "https://myfin.by/converter.html"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}


def find_course():
    global course_usd
    global course_eur
    global course_rub
    global course_pln
    global course_gbp
    global course_cny
    while True:
        response = requests.get(url=url, headers=headers)
        status = response.status_code
        if status == 200:
            content = response.content
            with open("folder/hw.html", "wb") as file:
                file.write(content)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.findAll("input", class_="input_calc form-control form-input-sum bestmb")
        new_data = str(data).split(sep='inputmode="decimal" type="tel" value="')
        new_data = str(new_data).split(sep='<input class="input_calc form-control form-input-sum bestmb" id="bestmb_')
        dollar1 = new_data[1].split("""', '""")[0].split('"')[0]
        dollar2 = new_data[1].split("""usd" ', '""")[1].split('"/>')[0]
        dollar = tuple([dollar2, dollar1])
        euro1 = new_data[2].split("""', '""")[0].split('"')[0]
        euro2 = new_data[2].split("""eur" ', '""")[1].split('"/>')[0]
        euro = tuple([euro2, euro1])
        rub1 = new_data[6].split("""', '""")[0].split('"')[0]
        rub2 = new_data[6].split("""rub" ', '""")[1].split('"/>')[0]
        rub = tuple([rub2, rub1])
        sterling1 = new_data[3].split("""', '""")[0].split('"')[0]
        sterling2 = new_data[3].split("""gbp" ', '""")[1].split("/>,")[0].split('"')[0]
        sterling = tuple([sterling2, sterling1])
        zloty1 = new_data[5].split("""', '""")[0].split('"')[0]
        zloty2 = new_data[5].split("""pln" ', '""")[1].split('"/>')[0]
        zloty = tuple([zloty2, zloty1])
        uany1 = new_data[4].split("""', '""")[0].split('"')[0]
        uany2 = new_data[4].split("""cny" ', '""")[1].split('"/>')[0]
        uany = tuple([uany2, uany1])
        cours = [dollar, euro, rub, sterling, zloty, uany]
        value = 1

        for valute in cours:
            if valute[-1] == "usd":
                course_usd = float(valute[0])
                result = value * float(valute[0])
                result = round(result, 3)
                print(result)

            if valute[-1] == "eur":
                course_eur = float(valute[0])
                result = value * float(valute[0])
                result = round(result, 3)
                print(result)

            if valute[-1] == "rub":
                course_rub = float(valute[0])
                result = value * float(valute[0])
                result = round(result, 3)
                print(result)

            if valute[-1] == "gbp":
                course_gbp = float(valute[0])
                result = value * float(valute[0])
                result = round(result, 3)
                print(result)

            if valute[-1] == "cny":
                course_cny = float(valute[0])
                result = value * float(valute[0])
                result = round(result, 3)
                print(result)

            if valute[-1] == "pln":
                course_pln = float(valute[0])
                result = value * float(valute[0])
                result = round(result, 3)
                print(result)

    else:
        print("Error...")
    new_course = int(dt.datetime.now().strftime("%S"))
    print(new_today)
    if new_course % 10 != 0:
        time.sleep(10)
    print("Course has been updated.")

Thread(target=find_course).start()


class HomePage(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.label1 = QLabel()
        layout.addWidget(self.label1)

        self.label2 = QLabel()
        layout.addWidget(self.label2)

        self.label3 = QLabel()
        layout.addWidget(self.label3)

        self.label4 = QLabel()
        layout.addWidget(self.label4)

        self.line_edit.textChanged.connect(self.line_edit_text_changed1)
        self.line_edit.textChanged.connect(self.line_edit_text_changed2)
        self.line_edit.textChanged.connect(self.line_edit_text_changed3)
        self.line_edit.textChanged.connect(self.line_edit_text_changed4)
        self.line_edit.textChanged.connect(self.line_edit_text_changed5)
        self.line_edit.textChanged.connect(self.line_edit_text_changed6)

        self.show()

    def line_edit_text_changed1(self, text):
        text = course_eur * float(text)
        self.label.setText("Your money: " + str(text) + " dollars")

    def line_edit_text_changed2(self, text):
        text = course_eur * float(text)
        self.label.setText("Your money: " + str(text) + "euros")

    def line_edit_text_changed3(self, text1):
        text1 = course_rub * float(text1)
        self.label1.setText("Your money: " + str(text1) + "rubles")

    def line_edit_text_changed4(self, text2):
        text2 = course_cny * float(text2)
        self.label2.setText("Your money: " + str(text2) + " yuans")

    def line_edit_text_changed5(self, text3):
        text3 = course_gbp * float(text3)
        self.label3.setText("Your money: " + str(text3) + " sterlings")

    def line_edit_text_changed6(self, text4):
        text4 = course_pln * float(text4)
        self.label4.setText("Your money: " + str(text4) + " zlotys")


app = QApplication(sys.argv)
mw = HomePage()
app.exec()




