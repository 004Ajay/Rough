from tkinter import *
from tkinter import messagebox

def login():
    if username.get() == "admin" and password.get() == "admin":
        messagebox.showinfo("Login", "Welcome Admin")
    else:
        messagebox.showinfo("Login", "Invalid username or password")

root = Tk()
root.title("Login")
root.geometry("300x300")

username = StringVar()
password = StringVar()

Label(root, text="Username").grid(row=0, column=0)
Entry(root, textvariable=username).grid(row=0, column=1)
Label(root, text="Password").grid(row=1, column=0)
Entry(root, textvariable=password).grid(row=1, column=1)
Button(root, text="Login", command=login).grid(row=2, column=1)

root.mainloop()