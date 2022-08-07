import random
from unicodedata import name

movies = [
          'trance', 'forensic', 'shylock', 'the kung fu master', 'big brother', 'lucifer', 'brothers day',
          'cold case', 'cbi', 'one', 'home', 'the priest', 'malik', 'the great indian kitchen', 'salute',
          'joseph', 'night drive', 'traffic', 'classmates', 'bangalore days', 'sunny', 'joji', 'take off',
          'godfather', 'ramji rao speaking', 'his highness abdullah', 'uncle bun', 'johny walker', 'hitler',
          'superman', 'the car', 'summer in bethlehem', 'punjabi house', 'crime file', 'friends'
         ]

def create_question(movie): # for making packed form of taken movie, eg: for cbi -> *** (packing as stars)
    temp = []
    for i in list(movie):
        if i == ' ':
            temp.append(' ') # for space b\w words of taken movie name
        else:
            temp.append('*') # for letters in movie name
    qn = ''.join(str(x) for x in temp)
    print(qn)
    return qn

def letter_unlock(qn, movie, letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if ref[i] == '' or ref[i] == letter:
            temp.append(ref[i])
        else:
            if qn_list[i] == '*':
                temp.append(' _ ')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new    

def main():
    print("\nMalayalam Movie Guessing Game\n\nOnly Malayalam movies with English title are included\n")
    picked_movie = random.choice(movies)
    qn = create_question(picked_movie)

    letter_guess(picked_movie)
    while True:
            letter_guess(picked_movie)
                ch = int(input("Press 1) guess movie's full name or 2) guess another letter: "))
                if ch == 1:
                    movie_guess(picked_movie)
                elif ch == 2:
                    letter_guess(picked_movie)
                else:
                    print(ch, "is out of range")
                    letter_guess(picked_movie, modified_qn)

if __name__ # define main function call                    