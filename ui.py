import time
from threading import Thread
from tkinter import *
import tkinter as tk
from .calc import *

import tkinter
import tkinter.ttk as ttk

root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello!").grid(column=0, row=0)
ttk.Button(frm, text="Cancel", command=root.destroy).grid(column=1, row=0)
root.mainloop()

from tkinter import *
from tkinter import ttk

hours = 0
minutes = 0
seconds = 0

pause = True


def stop_timer():
    global pause

    pause = False


def reset_timer():
    global hours
    hours = 0
    global minutes
    minutes = 0
    global seconds
    seconds = 0
    hours_label.config(text=f"{hours}")
    minuts_label.config(text=f"{minutes}")
    seconds_label.config(text=f"{seconds}")


def start_timer():
    global pause

    pause = True

    global hours

    global minutes

    global seconds


    while pause:
        seconds += 1

        if seconds > 59:
            minutes += 1
            seconds = 0

        if minutes > 59:
            hours += 1
            minutes = 0

        if hours > 23:
            seconds = 0
            minutes = 0
            hours = 0

        time.sleep(0.00001)

        hours_label.config(text=f"{hours}")
        minuts_label.config(text=f"{minutes}")
        seconds_label.config(text=f"{seconds}")
        print(f"{hours}:{minutes}" + ":" + str(seconds))


def start_new_thread():
    Thread(
        target=start_timer
    ).start()

start_new_thread()

start_new_thread

root = Tk()

frm = ttk.Frame(root, padding=100)
root.title("Таймер с интерфейсом на Python")
root.geometry("640x480")
frm.grid()

hours_label = ttk.Label(frm, text="00")
hours_label.grid(column=0, row=0)

ttk.Label(frm, text=":").grid(column=1, row=0)

minuts_label = ttk.Label(frm, text="00")
minuts_label.grid(column=2, row=0)

ttk.Label(frm, text=":").grid(column=3, row=0)

seconds_label = ttk.Label(frm, text="00")
seconds_label.grid(column=4, row=0)

Button(text="stop",
       background="#555",
       foreground="#ccc",
       padx="20",
       pady="8",
       font="16",
       command=stop_timer,
       ).grid(column=0, row=1)

Button(text="reset",
       background="#555",
       foreground="#ccc",
       padx="20",
       pady="8",
       font="16",
       command=reset_timer,
       ).grid(column=1, row=1)

Button(text="start",
       background="#555",
       foreground="#ccc",
       padx="20",
       pady="8",
       font="16",
       command=start_new_thread,
       ).grid(column=2, row=1)

ttk.Label(frm, text="Nick").grid(column=0, row=1)
ttk.Label(frm, text="Anna").grid(column=1, row=1)
ttk.Label(frm, text="Sveta").grid(column=2, row=1)

ttk.Label(frm, text="Hello!").grid(column=0, row=0)

ttk.Button(frm, text="Cancel", command=root.destroy).grid(column=1, row=0)

print_to_console = ("Well done!")

root.mainloop()