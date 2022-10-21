"""
1. make a gui using python which asks the user for username and password
2. when user enters the username and password, it should check the database entry of username and password
3. show an acceptance message, if user's entry matches with data in database, else show an error message
"""

from tkinter import *
import sqlite3

root = Tk()
root.geometry("400x400")
root.title("Login Form")

# create a database or connect to one
conn = sqlite3.connect('login.db')

# create cursor
c = conn.cursor()

# create table
'''
c.execute("""CREATE TABLE login (
            username text,
            password text
            )""")
'''

# create submit function for database
def submit():
    # create a database or connect to one
    conn = sqlite3.connect('login.db')
    # create cursor
    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO login VALUES (:username, :password)",
              {
                  'username': username.get(),
                  'password': password.get()
              })

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # clear the text boxes
    username.delete(0, END)
    password.delete(0, END)

# create query function
def query():
    # create a database or connect to one
    conn = sqlite3.connect('login.db')
    # create cursor
    c = conn.cursor()

    # query the database
    c.execute("SELECT *, oid FROM login")
    records = c.fetchall()
    # print(records)

    # loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # close connection
    conn.close()

# create text boxes
username = Entry(root, width=30)
username.grid(row=1, column=1, padx=20)
password = Entry(root, width=30)
password.grid(row=2, column=1, padx=20)

# create text box labels
username_label = Label(root, text="Username")
username_label.grid(row=1, column=0)
password_label = Label(root, text="Password")
password_label.grid(row=2, column=0)

# create submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=20)

# create a query button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=20)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()