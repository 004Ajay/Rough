from pprint import pprint
from unicodedata import name


stack = []

def push():
    lim = int(input("Enter limit: "))
    for i in range(lim):
        stack.append(input("Enter value: "))

def display():
    print(stack)

def main():
    while True:
        choice = int(input("Choose any option\n1.PUSH\n2.POP\n3.DISPLAY\n4.EXIT\nChoice: "))
        if choice == 1:
            push()
        elif choice == 3:
            display()
        if input("Continue? y/n : ") != 'y':
            break    

if __name__ == "__main__":
    main()    
    
    