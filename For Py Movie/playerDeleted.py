import random

movies = [
          'trance', 'forensic', 'shylock', 'the kung fu master', 'big brother', 'lucifer', 'brothers day',
          'cold case', 'cbi', 'one', 'home', 'the priest', 'malik', 'the great indian kitchen', 'salute',
          'joseph', 'night drive', 'traffic', 'classmates', 'bangalore days', 'sunny', 'joji', 'take off',
          'godfather', 'ramji rao speaking', 'his highness abdullah', 'uncle bun', 'johny walker', 'hitler',
          'superman', 'the car', 'summer in bethlehem', 'punjabi house', 'crime file', 'friends'
         ]



def create_question(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range(n):
        if letters[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn = ''.join(str(x) for x in temp)
    return qn
    
def is_present(letter, movie):
    c=movie.count(letter)
    if c == 0:
        return False
    else:
        return True
        
def unlock(qn, movie, letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if ref[i]=='' or ref[i]==letter:
             temp.append(ref[i])
        else:
            if qn_list[i]=='*':
                temp.append(' _ ')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new
    
def play():
    print("Malayalam Movie Guessing Game\nOnly Malayalam movies with English title are included")
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print (qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Your letter: ")
                if(is_present(letter, picked_movie)):
                    modified_qn=unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    d=input("Press 1 to guess the movie or 2 to unlock another letter: ")
                    if d==1:
                        ans=input("Your answer: ")
                        if ans==picked_movie:
                            print("Correct Letter")
                            not_said=False
                        else:
                            print("Wrong Answer, Try again.")
                else:
                    print(letter, " not found")
            c=int(input("press 1 to Continue or 0 to Quit: "))
            if c==0:
                print("Thanks for playing.")
                willing=False
            else:
                picked_movie=random.choice(movies)
                qn=create_question(picked_movie)
                print (qn)
            
            not_said=True
            while not_said:
                letter=input("Your letter: ")
                if(is_present(letter, picked_movie)):
                    modified_qn=unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    d=input("Press 1 to guess the movie or 2 to unlock another letter: ")
                    if d==1:
                        ans=input("Your answer: ")
                        if ans==picked_movie:
                            print("Correct Letter")
                            not_said=False
                        else:
                            print("Wrong Answer, Try again.")
                else:
                    print(letter, " not found")
            c=int(input("press 1 to Continue or 0 to Quit: "))
            if c==0:
                print("Thanks for playing.")
                willing=False
        turn=turn+1
        
play()