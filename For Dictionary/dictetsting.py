# Python Program to simulate the working of a book stock keeping software

"""
update() - used to add new item to dictionary
in - used to check whether the dictionary has the element entered before 'in', eg: name in database
pop() - used to delete an entry from dictionary

"""

print("\n")
stock = {}

# Funtion to update file
book_file = open("Book.txt")
for line in book_file:
    key, value = line.split(":")
    stock[key] = value
book_file.close()
for i in stock.items():
    i.strip("\n")
print("contents:", stock)

book_files = open("Book.txt", "r+")
for key, value in stock.items():
    book_files.write(key)
    book_files.write(":")
    book_files.write(str(value))
#book_files.strip()
book_files.close()
print("Final List: ", stock)