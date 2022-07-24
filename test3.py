matrix1 = []
matrix2 = []

row = int(input("Enter the number of rows of 1st matrix: "))
column = int(input("Enter the number of columns of 1st matrix: "))

print("Enter the values of matrix 1, one by one (row-wise):")

for i in range(row):        # for loop for getting row values
    a =[]
    for j in range(column):     # for loop for getting column values
        a.append(int(input()))
    matrix1.append(a)

print("Enter the values of matrix 2, one by one (row-wise):")

for i in range(row):        # for loop for getting row values
    a =[]
    for j in range(column):     # for loop for getting column values
        a.append(int(input()))
    matrix2.append(a)

print("len: ", len(matrix1))