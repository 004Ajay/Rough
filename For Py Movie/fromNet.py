import random
Films=["Deadpool","Avengers Endgame","Drishyam","Justice League","Cars","Inception","Soul","Despicable Me"]

def create_question(Movie):    
    n=len(Movie)
    letters=list(Movie)
    temp=[]
    for i in range(n):
        if letters[i]== " ":
           temp.append(" ")
        else:
           temp.append("*")
    Q =" ".join(str(x) for x in temp)
    return Q

def is_present(letter,Movie):
    c=Movie.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(Q,picked_Movie,letter):
    ref=list(picked_Movie)
    Q_list=list(Q)
    temp=[]
    n=len(picked_Movie)
    for i in range(n):
        if ref[i]==" " or ref[i]==letter:
           temp.append(ref[i])
        else:
          if Q_list[i]=="*" or Q_list[i]==" ":
            temp.append(" _ ")
          else:
              temp.append(ref[i])
    
    Q_new ="".join(str(x) for x in temp)
    return Q_new         
            
            
            
    
    

def game():
    pA=input("Player 1 Name:")
    pB=input("Player 2 Name:")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            print(pA,",your turn")
            picked_Movie=random.choice(Films)
            Q=create_question(picked_Movie)
            print(Q)
            modified_Q=Q
            not_said=True 
            while not_said:
                letter=input("Your letter:")
                if(is_present(letter,picked_Movie)):
                    modified_Q = unlock(modified_Q,picked_Movie,letter)
                    print(modified_Q)
                    d=int(input("Press 1 to guess the movie or 2 to unlock another character"))
                    if d==1:
                        ans=input("Answer:")
                        if ans==picked_Movie:
                            print("Yay! Correct answer.")
                            pp1=pp1+1
                            print(pA,"'s Score=",pp1)
                            not_said=False
                        else:
                            print("Wrong Answer, Try again...")
                            
                            
                 
                else:
                    print(letter,'not found')
            c=int(input("press 1 to continue or 0 to exit:"))
            if c==0:
                print(pA,",Your Score is",pp1)
                print(pB,",Your Score is",pp2)
                print("Thank you for playing, have a nice day!!!")
                willing=False
                    
        else: 
            print(pB,",your turn")
            picked_Movie=random.choice(Films)
            print(picked_Movie)
            Q=create_question(picked_Movie)
            print(Q)
            modified_Q=Q
            not_said=True 
            while not_said:
                letter=input("Your letter:")
                if(is_present(letter,picked_Movie)):
                    modified_Q = unlock(modified_Q,picked_Movie,letter)
                    print(modified_Q)
                    d=int(input("Press 1 to guess the movie or 2 to unlock another character:"))
                    if d==1:
                        ans=input("Answer:")
                        if ans==picked_Movie:
                            print("Yay! Correct answer.")
                            pp2=pp2+1
                            print(pB,"'s Score=",pp2)
                            not_said=False
                        else:
                            print("Wrong Answer, Try again...")
                else:
                    print(letter,'not found')
            c=int(input("press 1 to continue or 0 to exit:"))
            if c==0:
                print(pA,",Your Score is",pp1)
                print(pB,",Your Score is",pp2)
                print("Thank you for playing, have a nice day!!!")
                willing=False
             
        turn=turn+1
game()         