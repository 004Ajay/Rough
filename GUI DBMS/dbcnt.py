import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database = 'data'
    )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM test3")

res = mycursor.fetchall()

for x in res:
    print(x)