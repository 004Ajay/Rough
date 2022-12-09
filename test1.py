# import the Tkinter module
import tkinter as tk

# create a new Tkinter window
window = tk.Tk()

# set the window title
window.title("Login Form")

# create a label for the username field
username_label = tk.Label(window, text="Username:")
username_label.pack()

# create an entry field for the username
username_entry = tk.Entry(window)
username_entry.pack()

# create a label for the password field
password_label = tk.Label(window, text="Password:")
password_label.pack()

# create an entry field for the password
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# create a login button
login_button = tk.Button(window, text="Login")
login_button.pack()

# start the Tkinter main loop
window.mainloop()
