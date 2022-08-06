import random

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
            
def unlock(qn, movie, letter):
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

def movie_guess(picked_movie):
    if input("Your answer: ") == picked_movie:
        print("Correct...")
        again()
    else:
        print("Wrong Answer, but go on...")



def letter_guess(picked_movie):
    letter = input("Your letter guess: ")
    if letter in picked_movie:
        modified_qn = unlock(modified_qn, picked_movie, letter)
        print(modified_qn)


def again():
    play() if input("Do you want to play again? y/n: ") == 'y' else exit()

def play():
    print("\nMalayalam Movie Guessing Game\n\nOnly Malayalam movies with English title are included\n")
    while True:
        picked_movie = random.choice(movies)
        qn = create_question(picked_movie)
        modified_qn = qn
        willing = True
        while willing:
            letter_guess(picked_movie)
                d = int(input("Press 1) guess movie's full name or 2) guess another letter: "))
                if d == 1:
                    movie_guess(picked_movie)
                elif d == 2:
                    letter_guess(picked_movie)
                else:
                    print(d, "is out of range")
                    letter_guess(picked_movie)
            else:
                print(letter, " not found")            
                
play()