import os

save_path = 'D:\Temp'

name_of_file = input("What is the name of the file: ")

completeName = os.path.join(save_path, name_of_file+".txt")         

file1 = open(completeName, "w")

toFile = input("Write what you want into the field")

file1.write(toFile)

file1.close()