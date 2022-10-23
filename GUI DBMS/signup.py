from tkinter import *
from tkinter import messagebox

def signup(): # function to make a sign up gui
    root = Tk()
    root.title("Sign Up")
    root.geometry("500x500")
    root.configure(background="white")

    #labels
    lbl_name = Label(root, text="Name", bg="white", fg="black", font=("Arial", 13))
    lbl_name.place(x=50, y=50)

    lbl_email = Label(root, text="Email", bg="white", fg="black", font=("Arial", 13))
    lbl_email.place(x=50, y=100)

    lbl_password = Label(root, text="Password", bg="white", fg="black", font=("Arial", 13))
    lbl_password.place(x=50, y=150)

    lbl_confirm_password = Label(root, text="Confirm Password", bg="white", fg="black", font=("Arial", 13))
    lbl_confirm_password.place(x=50, y=200)

    #entry
    entry_name = Entry(root, width=30)
    entry_name.place(x=200, y=50)

    entry_email = Entry(root, width=30)
    entry_email.place(x=200, y=100)

    entry_password = Entry(root, width=30)
    entry_password.place(x=200, y=150)

    entry_confirm_password = Entry(root, width=30)
    entry_confirm_password.place(x=200, y=200)

    #button
    btn_signup = Button(root, text="Sign Up", bg="white", fg="black", font=("Arial", 13), command=lambda: signup_check(entry_name.get(), entry_email.get(), entry_password.get(), entry_confirm_password.get()))
    btn_signup.place(x=200, y=250)

    root.mainloop()

def signup_check(name, email, password, confirm_password): # function to check the sign up details
    if name == "" or email == "" or password == "" or confirm_password == "":
        messagebox.showerror("Error", "Please fill all the details")
    elif password != confirm_password:
        messagebox.showerror("Error", "Confirmed Password does not match")
    else:
        messagebox.showinfo("Success", "Sign Up Successful")

signup()