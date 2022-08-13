import random

movies = ['def gh', 'kl mn']


def again():
    main() if input("Do you want to play again? y/n: ") == 'y' else exit()

"""
# unpack at final stage ------ //////// --------- /////// ----

def inst():
    print("\nMalayalam Movie Guessing Game.\n\nOnly Malayalam movies with English title are included.\n")
    if input("Let's start? (y/n): ") != 'y':
        print("Exited!\n") 
        exit()
"""        
    
def create_qn(movie): # for making packed form of picked movie, eg: cbi -> *** (packing as stars)
    temp = []
    for i in list(movie):
        temp.append(' ') if i == ' ' else temp.append('*') # if else shorthand
    return ''.join(str(x) for x in temp) # returing string after joining contents of list temp


def movie_guess(movie, modi_qn):
    if input("Your answer: ").lower() == movie:
        print("Correct...")
        again()
    else:
        print("Wrong Answer, but go on...")
        letter_guess(movie, modi_qn)


def letter_guess(movie, mod_qn):
    letter = input("Your letter guess: ").lower() # getting letter
    if letter in movie:
        print(f"Yes, {letter} found")
        ref = list(movie) # picked movie as list
        qn_list = list(mod_qn)    
        temp = []
        for i in range(len(movie)):
            #if ref[i] == ' ':
            #    temp.append(' ')
            if ref[i] == letter or ref[i] in mod_qn:
                temp.append(ref[i])
            elif qn_list[i] in ['*', '_']:
                temp.append('_')
        mod_qn = ''.join(str(x) for x in temp)
        print(mod_qn)    
        return mod_qn
    else:
        print(f"No, {letter} not found")

def getNum():
    try:
        numb = int(input("Press 1) Guess movie's full name or 2) Guess another letter or 3) Exit : "))
    except:
        print("Wrong Input. Try Again")
        numb = getNum()
    return numb


def main():
    # inst() un-comment in final stage ------ //////// --------- /////// ----
    while True:
        try:
            picked_movie = random.choice(movies)
            movies.remove(picked_movie) # removing currently selected movie to avoid repetition
            print(picked_movie) # remove at final change ------ //////// --------- /////// ----
            qn = create_qn(picked_movie)
            print(qn)
            modified_qn = qn
            while True:
                gus = letter_guess(picked_movie, modified_qn)
                modified_qn = gus
                num = getNum()
                if num == 1:
                    movie_guess(picked_movie, modified_qn)
                elif num == 2:
                    res = letter_guess(picked_movie, modified_qn)
                    modified_qn = res
                elif num == 3:
                    exit()    
                else:
                    print(num, "is out of range. Please guess another letter.")
                    resl = letter_guess(picked_movie, modified_qn)
                    modified_qn = resl            
        except:
            print("Sorry, List is empty.\nThank you for playing.\n")
            exit() if input("Can we exit? (y/n): ") == 'y' else print("\nNo steps ahead\n")

if __name__ == "__main__": # initiator
    main()