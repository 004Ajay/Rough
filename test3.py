matrix1, matrix2, matrix_sum = [], [], [] # declaring multiple lists

# Function for printing matrix
def print_matrix(matrix, row, column):
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end = " ")
        print()

# Function for getting matrix
def getMatrix(matrix, row, column):
    for i in range(row): # for loop for getting row values
        a =[]
    for j in range(column): # for loop for getting column values
        a.append(int(input()))
    matrix.append(a)

# Function for calculating sum of matrices
def calcSum(matrix_sum, matrix1, matrix2, row, column):
    for i in range(row):
        for j in range(column):
            matrix_sum[i][j] = matrix1[i][j] + matrix2[i][j] # adding matrices

def main():
    r, c = input("Enter the number of rows & columns: ").split() # getting multiple inputs
    row, column = int(r), int(c) # type casting from string to integer

    print("Enter the values of matrix 1, one by one (row-wise):")
    getMatrix(matrix1, row, column)
    print("Enter the values of matrix 2, one by one (row-wise):")
    getMatrix(matrix2, row, column)
    print("\nMatrix1:")    
    print_matrix(matrix1, row, column)
    print("\nMatrix2:")
    print_matrix(matrix2, row, column)    
    print("\nMatrix sum:")
    print_matrix(matrix_sum, matrix1, matrix2, row, column)

if __name__ == "__main__":
    main()    