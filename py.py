import random

def init():
    i = 10
    print(f"What is {random.randint(1, i)} + {random.randint(1, i)} ?")

def getAns():
    ans = int(input("Your opinion: "))
    if ans == random.randint(1, i) + random.randint(1, i):
        print("ANSWER IS CORRECT")
    else:
        print("ANSWER IS WRONG")