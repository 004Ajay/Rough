def FizzBuzz(lst):
    a=[]
    for i in lst:
        if i % 3 == 0 and i % 5 == 0:
            a.append("FizzBuzz")
        elif i % 3 == 0:
            a.append("Fizz")
        elif i % 5 == 0:
            a.append("Buzz")
        else:    
            a.append(str(i))
    return a
n = int(input())
print(FizzBuzz(n))