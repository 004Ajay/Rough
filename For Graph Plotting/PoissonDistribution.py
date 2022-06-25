# Question: Write a program to calculate for the formula {(λ^k)*(e^-λ)} ÷ k!

def checkFactorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

lamb = float(input("Enter the value of lambda: "))
k = int(input("Enter the value of k: "))

numerator = (lamb**k)*(2.7**(-1*lamb))
denominator = checkFactorial(k)
result = float(numerator/denominator)
print("value: ", result)