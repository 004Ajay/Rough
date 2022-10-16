"""
make a timer gui with pause, resume, reset and stop functionality in python
"""

from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Timer")

def start():
    global running
    running = True
    timer()

def stop():
    global running
    running = False

def reset():
    global running
    running = False
    time_string = "00:00:00"
    clock.config(text=time_string)

def pause():
    global running
    running = False

def timer():
    if running:
        global timer
        # get the current local time from the PC
        current_time = time.strftime("%H:%M:%S")
        # if time string has changed, update it
        clock.config(text=current_time)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(200, timer)

clock = Label(root, font=("times", 50, "bold"), bg="green")
clock.grid(row=0, column=1)

start_button = ttk.Button(root, text="Start", command=start)
start_button.grid(row=1, column=0)

stop_button = ttk.Button(root, text="Stop", command=stop)
stop_button.grid(row=1, column=1)

reset_button = ttk.Button(root, text="Reset", command=reset)
reset_button.grid(row=1, column=2)

pause_button = ttk.Button(root, text="Pause", command=pause)
pause_button.grid(row=1, column=3)

root.mainloop()