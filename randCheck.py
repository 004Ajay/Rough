import random

def start(i):
    print(f"What is {random.randint(1, i)} + {random.randint(1, i)} ?")

def getAns(ans, j):
    if ans == random.randint(1, j) + random.randint(1, j):
        print("ANSWER IS CORRECT")
    else:
        print("ANSWER IS WRONG")