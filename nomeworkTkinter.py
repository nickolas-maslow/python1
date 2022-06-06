from tkinter import *
from tkinter import ttk


def alright():
    print("Все работает хорошо.")


root = Tk()  # создание объекта ткинтер

frm = ttk.Frame(root, padding=10)  # создание главного окна
root.title("Большая кнопка")
root.geometry("640x480")  # размер окна
frm.pack()

Button(text="Эта кнопка",  # текст кнопки
       background="grey",  # фон кнопки
       foreground="black",  # цвет текста
       padx="20",  # отступ по горизонтали
       pady="8",  # отступ по вертикали
       font="16",  # высота шрифта
       command=alright).pack()

root.mainloop()
