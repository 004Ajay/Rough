# PYTHON PROGRAM TO CHECK THE VALIDITY OF AN EMAIL BY VERIFYING IT'S FORMAT

firstHalf = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
vendor = 'gmail, icloud, github, sjcet, outlook' # just a sample items
domain = 'com, in, ac, ac.in, net'

def checkmail():
    part_one = email.split('@') # now email splitted into 'ajaytshaju', 'gmail.com' // output: ['ajaytshaju', 'gmail.com']
    part_two = part_one[1].split('.') # now 'gmail.com' becomes 'gmail', 'com' // output: ['gmail', 'com']

    for i in part_one[0]: # checking first half i.e 'ajaytshaju'
        print("Invalid Email, Problem in first half") if i not in firstHalf else return 0
        

    for j in part_two[0]: # checking middle half of 'gmail.com' which is 'gmail'
        if j not in vendor:
            print("Invalid Email, Problem in middle half")
            return 0

    for k in part_two[1]: # checking second half of 'gmail.com' which is 'com'
        if k not in domain:
            print("Invalid Email, Problem in last half")
            return 0
    return 1 # no errors found in the input email                  

while True: # for recurrent inputting
    email = input("Enter an Email: ") # getting email, eg - ajaytshaju@gmail.com
    
    if "@" in email: # checking for '@'
        if "." in email: # checking for '.'
            print("Valid Email") if checkmail() else None  # passes every checking, if-else shorthand used  
    if input("Again? y/n ") == 'n':
        break