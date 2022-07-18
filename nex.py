import random
i = 10
print(f"{random.randint(1, i)} + {random.randint(1, i)} = ")

ans = int(input("Your opinion: "))

if ans == random.randint(1, i) + random.randint(1, i):
    print("ANSWER IS CORRECT")
else:
    print("ANSWER IS WRONG")    