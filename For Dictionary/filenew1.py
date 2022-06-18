stock = {}

book_file = open("Book.txt", "r+")
for line in book_file:
   key, value = line.split(":")
   stock.update(key)

print("Existing List: ", stock)

book_files = open("Book.txt", "r+")

for key, value in stock.items():
    book_files.write('%s:%s' % (key, value))

book_files.close()

print("Final List: ",stock)