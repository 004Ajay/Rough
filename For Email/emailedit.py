# PYTHON PROGRAM TO CHECK THE VALIDITY OF AN EMAIL BY VERIFYING ITS FORMAT

first_half = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
middle_half = 'gmail, hotmail, yahoo, icloud, github, sjcet, outlook'
last_half = 'com, in, ac, ac.in, net'

def checkmail(): # return value: 1 == error, 0 = no error

    part_one = email.split('@') # now email splitted into 'ajaytshaju', 'gmail.com'
    part_two = part_one[1].split('.') # now 'gmail.com' becomes 'gmail', 'com'

    for i in part_one[0]: # checking first half i.e 'ajaytshaju'
        if i not in first_half:
            print("Invalid Email, Problem in first half")
            return 1

    for j in part_two[0]: # checking middle half of 'gmail.com' which is 'gmail'
        if j not in middle_half:
            print("Invalid Email, Problem in middle half")
            return 1

    for k in part_two[1]: # checking second half of 'gmail.com' which is 'com'
        if k not in last_half:
            print("Invalid Email, Problem in last half")
            return 1

    return 0 # no errors found in the input email                  

while True:
    email = input("Enter email: ") # getting email, eg - ajaytshaju@gmail.com
    
    if "@" in email: # checking for '@'
        if "." in email: # checking for '.'
            value = checkmail()
            if value == 0: # if no error, 1 won't be returned
                print("Valid Email") # it passes every levels of checking
            elif value == 1:
                None    
    if input("Again? y/n ") == 'n':
        break