import random

steps = 0
lst = [1,5,3,2,4]
new_lst = []

while new_lst == sorted(lst):
    srt_lst = random.shuffle(lst)
    new_lst.append(srt_lst)
    print(lst)
    step += 1
    
print(f"Original list: {lst}\nSorted list: {new_lst}\nNumber of steps: {steps}")