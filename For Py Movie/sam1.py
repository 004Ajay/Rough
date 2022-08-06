import random

movies = [
          'trance', 'forensic', 'shylock', 'the kung fu master', 'big brother', 'lucifer', 'brothers day',
          'cold case', 'cbi', 'one', 'home', 'the priest', 'malik', 'the great indian kitchen', 'salute',
          'joseph', 'night drive', 'traffic', 'classmates', 'bangalore days', 'sunny', 'joji', 'take off',
          'godfather', 'ramji rao speaking', 'his highness abdullah', 'uncle bun', 'johny walker', 'hitler',
          'superman', 'the car', 'summer in bethlehem', 'punjabi house', 'crime file', 'friends'
         ]

def pick_movie():
    ans = random.choice(movies)
    n = len(ans)
    return ans, n


def guess():
    word = ''
    ans, n = pick_movie()    
    print(f"movie name: {ans}\nIt's length: {n}")

    for i in range(n):
        print(" _ ", end = " ")

    letter = input("\nYour letter guess: ")

    while ans:
        for i in range(n):
            if letter == ans[i]:
                print(f"Yes, {letter} found")
                word += letter
                guess()
            else:
                print(f"No, {letter} not found") 
                word += ' _ ' 
                guess()
                break        
    print(word)

guess()    
"""
# PYTHON PROGRAM TO REPLACE A WORD IN A SENTENCE BY ANOTHER WORD

sen = input("Enter the sentence: ")
del_word = input("Enter the word to delete: ")
replace_word = input("Enter the word to replace: ")
new_sen = ''

search = sen.split()

for i in search:
    if(i == del_word):
        new_sen += replace_word
    else:
        new_sen += i
print(new_sen)

"""        