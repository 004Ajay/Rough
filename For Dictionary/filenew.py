#details = {'The Brain': '30', 'Hooked': '150', 'Quiet': '70'}
stock = {}
"""
for key, value in details.items():
    f.write('%s:%s\n' % (key, value))
"""
f = open("myfile.txt", 'r+')

ls_key = []
ls_value = []

for line in f:
       key, value = line.split(":")
       ls_key.append(key)
       ls_value.append(value)
       #print(f'{key} {value}')


for book, value in ls_key, ls_value:
    stock.update({book:value})

print("Existing List: ", stock)
f.close()