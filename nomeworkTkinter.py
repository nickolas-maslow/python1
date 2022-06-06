from tkinter import *
from tkinter import ttk


def alright():
    print("Everything is fine.")


root = Tk()  # создание объекта ткинтер

frm = ttk.Frame(root, padding=10)  # создание главного окна
root.title("big button")
root.geometry("640x480")  # размер окна
frm.grid()  # cетка

Button(text="Button",  # текст кнопки
       background="#000000",  # фон кнопки
       foreground="#FFFFFF",  # цвет текста
       padx="20",  # отступ по горизонтали
       pady="8",  # отступ по вертикали
       font="16",  # высота шрифта
       command=alright).grid(column=3, row=5)

root.mainloop()
