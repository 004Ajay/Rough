from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Countdown Timer")

def countdown():
    t = int(entry_box.get())
    if t <= 0:
        reset()
        return
    else:
        global time_string
        while(t):
            mins, secs = divmod(t, 60)
            #current_time = '{:02d}:{:02d}'.format(mins, secs)
            #times = '{:02d}:{:02d}'.format(mins, secs)
            #current_time = strftime(f'{mins}:{secs}')
            #current_time = time.strftime("%M:%S")
            #current_time = '{:02d}:{:02d}'.format(mins, secs)
            current_time = (f'{mins}:{secs}')
            if current_time != time_string:
                time_string = current_time
                clock.config(text=time_string)
            
            #print(timeformat, end='\r')
            #time.sleep(1)
            clock.after(1000, countdown)
            t -= 1
            
            

def start():
    global running
    running = True
    #timer()
    countdown()

def stop():
    global running
    running = False

def reset():
    global running
    running = False
    time_string = "0"
    clock.config(text=time_string)

def exit():
    root.destroy()

clock = Label(root, font=("times", 50, "bold"))
clock.grid(row=0, column=1)

start_button = ttk.Button(root, text="Start", command=start)
start_button.grid(row=2, column=0, padx=5, pady=5)

stop_button = ttk.Button(root, text="Stop", command=stop)
stop_button.grid(row=2, column=1, padx=5, pady=5)

reset_button = ttk.Button(root, text="Reset", command=reset)
reset_button.grid(row=2, column=2, padx=5, pady=5)

exit_button = ttk.Button(root, text="Exit", command=exit)
exit_button.grid(row=2, column=3, padx=5, pady=5)

entry_label = ttk.Label(root, text="Enter Time in Seconds:")
entry_label.grid(row=1, column=0, padx=5, pady=5)

entry_box = ttk.Entry(root, width=10)
entry_box.grid(row=1, column=1, padx=5, pady=5)

#set_button = ttk.Button(root, text="Set", command=countdown)
#set_button.grid(row=1, column=2, padx=5, pady=5)

time_string = "0"
clock.config(text=time_string)

root.mainloop()