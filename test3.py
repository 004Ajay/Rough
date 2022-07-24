from tokenize import cookie_re


matrix1 = []
matrix2 = []

# Function for printing matrix
def print_matrix(matrix, row, column):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end = " ")
        print()


r, c = input("Enter the number of rows & columns: ").split() # getting multiple inputs
row, column = int(r), int(c) # type casting from string to integer

print("Enter the values of matrix 1, one by one (row-wise):")

for i in range(int(row)):        # for loop for getting row values
    a =[]
    for j in range(int(column)):     # for loop for getting column values
        a.append(int(input()))
    matrix1.append(a)

print("Enter the values of matrix 2, one by one (row-wise):")

for i in range(row):        # for loop for getting row values
    a =[]
    for j in range(column):     # for loop for getting column values
        a.append(int(input()))
    matrix2.append(a)

print("\nMatrix1:")    
print_matrix(matrix1, int(row), int(column))
print("\nMatrix2:")
print_matrix(matrix2, row, column)    

print("len: ", len(matrix1))