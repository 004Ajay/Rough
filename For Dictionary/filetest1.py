file = open("new.txt", "w")

my = {"name": 200, "country": 500}

ls=[]
for i, j in my.items():
    ls.append(f'{i}:{j}')
    
print(ls)

for k in ls:
    file.write(ls)

file.read()

file.close()