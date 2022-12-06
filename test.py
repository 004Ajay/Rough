"//get unique prime numbers from a list of 150 random numbers in python?"
for num in range(2,101):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)


for num in range(2,101):
    if all(num%i!=0 for i in range(2,num)):
       print (num)


import math
for num in range(2,101):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       print (num)


import math
print 2
for num in range(3,101,2):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       print (num)


import math
print 2
for num in range(3,101,2):
    if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
        print (num)


