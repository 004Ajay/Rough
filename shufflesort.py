import random

steps = 0
lst = [1,5,3,2,4]
new_lst = []

while new_lst != sorted(lst):
    srt_lst = random.shuffle(lst)
    print(lst, end=" ")
    steps += 1
    if steps >= 100 and new_lst != sorted(lst):
        new_lst.append("NULL")
        break
    elif new_lst != sorted(lst):
        new_lst.append(srt_lst)
        break
    
print(f"\nOriginal list: {lst}\nSorted list: {new_lst}\nNumber of steps: {steps}")