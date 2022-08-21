import random


movies = ['def gh']#, 'kl mn']


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
        if mod_qn == movie: # user fills the question by gussing each letters
            print("Correct...You guessed it...\n", mod_qn)
            again()
        else:
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


def movie_guess(movie, modi_qn):
    if input("Your answer: ").lower() == movie:
        print("Correct...You guessed it...\n", movie)
        again()
    else:
        print("Wrong Answer, but go on...")
        gus = letter_guess(movie, modi_qn)
        return gus


def again():
    main() if input("Do you want to play again? y/n: ") == 'y' else exit()


def main():
    # inst() un-comment in final stage ------ //////// --------- /////// ----
    while True:
        picked_movie = random.choice(movies)
        movies.remove(picked_movie) # removing currently selected movie to avoid repetition, works in multiple plays at one go
        print(picked_movie) # remove at final change ------ //////// --------- /////// ----
        qn = create_qn(picked_movie)
        print(qn)
        modified_qn = qn
        while True:
            gus = letter_guess(picked_movie, modified_qn)
            modified_qn = gus
            num = getNum()
            if num == 1:
                guss = movie_guess(picked_movie, modified_qn)
                modified_qn = guss
            elif num == 2:
                res = letter_guess(picked_movie, modified_qn)
                modified_qn = res
            elif num == 3:
                exit()    
            else:
                print(num, "is out of range. Please guess another letter.")
                resl = letter_guess(picked_movie, modified_qn)
                modified_qn = resl            

if __name__ == "__main__": # main function call
    main()


# check for num == 2 step error
# modify the code better     