a_dictionary = {}

a_file = open("data.txt")

for line in a_file:
    key, value = line.split(":")

    a_dictionary[key] = value

for key, value in a_dictionary.items():
    print(key, ' : ', value, end ="")

    """
    with open("BookStock.txt", 'w') as file_update:
	for key, value in details.items():
		file_update.write('%s:%s\n' % (key, value))
    """    