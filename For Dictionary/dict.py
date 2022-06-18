# Python Program to simulate the working of a book stock keeping software

"""
update() - used to add new item to dictionary
in - used to check whether the dictionary has the element entered before 'in', eg: name in database
pop() - used to delete an entry from dictionary

"""

print("\n")
stock = {}

# Funtion to update file
def rewrite_file_ToDict():
    book_file = open("BookStock.txt")
    for line in book_file:
       key, value = line.split(":")
       stock[key] = value
    book_file.close()

def rewrite_file_FromDict():
    book_file = open("BookStock.txt", "r+")

    for key, value in stock.items():
        book_file.write(key)
        book_file.write(":")
        book_file.write(str(value))
        book_file.write(" ")
    book_file.close()
    print("Final List: ", stock)
       
    

"""
# Funtion to update file
def add_file(update_book, count):
    with open("BookStock.txt", "a") as up_file: # opening file in append mode
        up_file.write() # writing to file and auto closing

# Function to show file contents
def show_file():
    for key, value in stock.items():
        print(key, ':', value, end="") 
"""

# Function to update stocks
def stock_updation():
    while True:  
        print(stock) # shwoing list for giving name in next line
        update_book = input("Enter book name to update: ")
        if update_book in stock: # checks if book exist in dictionary
            count = int(input("Enter book count: "))
            stock[update_book] = count  # changes value of corresponding book
            # add_file(update_book, count)

            print("\nUpdation Successful\nNew List: ", stock)
            """
            for key, value in stock.items():
                print(key, ':', value, end = "") # print code updated here only
            """
            if input("\nUpdating Again? y/n : ") != 'y':
                break
        else:
            print("No such book found.")
            if input("Trying again? y/n : ") != 'y':
                break

# Function to add new stocks
def stock_addition():
    while True:
        new_book = input("Enter book name to add: ")
        value = int(input("Enter new quantity: "))
        stock.update({new_book:value}) # adds new book to stock using update()
        print("Addition Successful\nNew List: ", stock)

        if input("Adding again? y/n : ") != 'y':
            break
            
# Function to delete a stock completely
def full_deletion():
    while True:
        print(stock) # shwoing list for giving name in next line
        del_book = input("Enter name of book to delete: ")
        if del_book in stock: # checks if book exist in dictionary
            stock.pop(del_book) # deletes the entry using pop()
            print("Deletion Successful\nNew List: ", stock)

            if input("Deleting Again? y/n : ") != 'y':
                break
        else:
            print("No such book found.")
            if input("Trying again? y/n : ") != 'y':
                break
 
# __Driver Code__
rewrite_file_ToDict()
while True:
 print("Existing List: ", stock)     
 print("\n1: Stock Updation\n2: New Stock Addition\n3: Full Deletion\n4: List view\n")
 choice = int(input("choice: "))

 if choice == 1:
     stock_updation()

 elif choice == 2:
     stock_addition()

 elif choice == 3:
     full_deletion()

 elif choice == 4:
     print(stock)
     #show_file()

 else:
     print("Choice is out of range")

 if input("\nAll Again? y/n : ") != 'y':
    rewrite_file_FromDict()
    break