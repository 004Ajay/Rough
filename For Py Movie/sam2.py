import random

movies = [
          'trance', 'forensic', 'shylock', 'the kung fu master', 'big brother', 'lucifer', 'brothers day',
          'cold case', 'cbi', 'one', 'home', 'the priest', 'malik', 'the great indian kitchen', 'salute',
          'joseph', 'night drive', 'traffic', 'classmates', 'bangalore days', 'sunny', 'joji', 'take off',
          'godfather', 'ramji rao speaking', 'his highness abdullah', 'uncle bun', 'johny walker', 'hitler',
          'superman', 'the car', 'summer in bethlehem', 'punjabi house', 'crime file', 'friends'
         ]


def create_qn(movie): # for making packed form of picked movie, eg: cbi -> *** (packing as stars)
    temp = []
    for i in list(movie):
        temp.append(' ') if i == ' ' else temp.append('*') # if else shorthand
    return ''.join(str(x) for x in temp) # returing string after joining contents of list temp


def unlock(qn, movie, letter): # qn = mod_qn, movie = picked_movie, letter = user input letter
    ref = list(movie) # picked movie as list
    qn_list = list(qn) # previously modified qn as list
    temp = []
    for i in range(len(movie)):
        if ref[i] == ' ':
            temp.append(' ')
        elif ref[i] == letter:
            temp.append(ref[i])
        elif qn_list[i] == '*' or qn_list[i] == '_' or qn_list[i] == ' _ ':
            temp.append(' _ ')
    return ''.join(str(x) for x in temp)


def movie_guess(picked_movie, modi_qn):
    if input("Your answer: ") == picked_movie:
        print("Correct...")
        again()
    else:
        print("Wrong Answer, but go on...")
        letter_guess(picked_movie, modi_qn)


def letter_guess(picked_movie, mod_qn):
    letter = input("Your letter guess: ")
    if letter in picked_movie:
        print(f"Yes, {letter} is found")
        mod_qn = unlock(mod_qn, picked_movie, letter)
        print(mod_qn)
    else:
        print(f"No, {letter} not found")    


def again():
    play() if input("Do you want to play again? y/n: ") == 'y' else exit()


def play():
    print("\nMalayalam Movie Guessing Game\n\nOnly Malayalam movies with English title are included\n")
    while True:
        picked_movie = random.choice(movies)
        print(picked_movie)
        qn = create_qn(picked_movie)
        print(qn)
        modified_qn = qn
        while True:
            letter_guess(picked_movie, modified_qn)
            d = int(input("Press 1) guess movie's full name or 2) guess another letter or 3) Exit : "))
            if d == 1:
                movie_guess(picked_movie, modified_qn)
            elif d == 2:
                letter_guess(picked_movie, modified_qn)
            elif d == 3:
                exit()    
            else:
                print(d, "is out of range")
                letter_guess(picked_movie, modified_qn)


play() # initiator

# use try catch for entering alphabets when int input is required.
# show previous correctly guessed letter
# add comment - chnage unlock func with other elifs