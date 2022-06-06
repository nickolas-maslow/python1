import time
time.sleep(secs=0.0001)

from tkinter import *

import tkinter as tk

from .calc import *
calc

from.import calc
calc.result


from tkinter import *
from tkinter import ttk
import time
from threading import Thread

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
    hours_lable.config(text=f"{hours}")
    minutes_lable.config(text=f"{minutes}")
    seconds_lable.config(text=f"{seconds}")

def start_timer():
    global pause
    pause = True

    global hours
    # hours = 0
    global minutes
    # minutes = 0
    global seconds
    # seconds = 0

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
        time.sleep(0.0001)
        hours_lable.config(text=f"{hours}")
        minutes_lable.config(text=f"{minutes}")
        seconds_lable.config(text=f"{seconds}")
        print(f"{hours}:{minutes}:{seconds}")


def start_new_thread():
    Thread(target=start_timer).start()

root = Tk()

frm = ttk.Frame(root, padding=10)
root.title("Таймер Python")
root.geometry("640x480")
frm.grid()

hours_lable = ttk.Label(frm, text="00")
hours_lable.grid(column=0, row=0)

ttk.Label(frm, text=":").grid(column=1, row=0)

minutes_lable = ttk.Label(frm, text="00")
minutes_lable.grid(column=2, row=0)

ttk.Label(frm, text=":").grid(column=3, row=0)

seconds_lable = ttk.Label(frm, text="00")
seconds_lable.grid(column=4, row=0)


Button(text="stop",
       background="#555",
       foreground="#ccc",
       padx="20",
       pady="8",
       font="16",
       command=stop_timer).grid(column=0, row=1)

Button(text="reset",
       background="#555",
       foreground="#ccc",
       padx="20",
       pady="8",
       font="16",
       command=reset_timer).grid(column=1, row=1)


Button(text="start",
       background="#555",
       foreground="#ccc",
       padx="20",
       pady="8",
       font="16",
       command=start_new_thread).grid(column=2, row=1)

root.mainloop()

