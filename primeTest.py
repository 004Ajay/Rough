lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("List contents:",lst)
print("Prime numbers: ", end="")

for j in lst:
    if j > 0:
        for i in range(2, j):
            if j % i == 0:
                break
        else:
            print(j, end = " ")