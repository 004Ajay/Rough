# This program convert input word to English alphabet number
# eg: a = 1, b = 2 then,  ab = 1 2
from traceback import print_tb


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # a to z
alpha_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] # 1 to 26

dic = dict(zip(alpha, alpha_num))
print(dic)



"""

lst = []

for i in range(len(alpha)):
    res = { alpha[i] : alpha_num[i] }
    lst.append(res)

print(lst)

"""



# word = input("Enter the word: ").lower()

# print(tuple(zip(alpha, alpha_num)))

# for i in word:
