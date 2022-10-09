from tkinter import *
from tkinter import ttk

root = Tk()

# create a label
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack()

# create a button
button = ttk.Button(root, text="Click Me!")
button.pack()

# create a textbox
textbox = ttk.Entry(root, width=30)
textbox.pack()
textbox.insert(0, "Enter your name: ")

# create a checkbox
checkbox = ttk.Checkbutton(root, text="Check this box!")
checkbox.pack()

# create a radio button
radio_button1 = ttk.Radiobutton(root, text="Option 1")
radio_button1.pack()
radio_button2 = ttk.Radiobutton(root, text="Option 2")
radio_button2.pack()

# create a combobox
combobox = ttk.Combobox(root,
                        values=[
                            "Monday",
                            "Tuesday",
                            "Wednesday",
                            "Thursday",
                            "Friday",
                            "Saturday",
                            "Sunday"
                        ])
combobox.current(0)

root.mainloop()