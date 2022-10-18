from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect( # connecting to database
    host="localhost",
    user="root",
    passwd="1234",
    database="project",
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

root = Tk()
root.title("Project")
root.geometry("500x500")
# root.geometry("1920x1080")

def insert():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    sql = "INSERT INTO customers (name, email, phone, address) VALUES (%s, %s, %s, %s)"
    val = (name, email, phone, address)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Data Inserted Successfully")

def show():
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

label_name = Label(root, text="Name")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_email = Label(root, text="Email")
label_email.grid(row=1, column=0, padx=10, pady=10)

entry_email = Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

label_phone = Label(root, text="Phone")
label_phone.grid(row=2, column=0, padx=10, pady=10)

entry_phone = Entry(root)
entry_phone.grid(row=2, column=1, padx=10, pady=10)

label_address = Label(root, text="Address")
label_address.grid(row=3, column=0, padx=10, pady=10)

entry_address = Entry(root)
entry_address.grid(row=3, column=1, padx=10, pady=10)

button_insert = Button(root, text="Insert", command=insert)
button_insert.grid(row=4, column=0, padx=5, pady=5)

button_show = Button(root, text="Show", command=show)
button_show.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()