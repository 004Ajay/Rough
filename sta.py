stack = []

def push():
    lim = int(input("Enter number of element to push: "))
    for i in range(lim):
        stack.append(int(input("Enter value: ")))

def main():
    while True:
        choice = int(input("Choose any option\n1.PUSH\n2.POP\n3.DISPLAY\n4.EXIT\nChoice: "))
        if choice == 1:
            push()
        elif choice == 2:
            print("Stack is empty") if len(stack) == 0 else print("Popped Element: ", stack.pop())
        elif choice == 3:
            print("Stack is empty") if len(stack) == 0 else print(stack)
        elif choice == 4:
            print("Exited!\n")
            exit()    
        if input("Continue? y/n : ") != 'y':
            break    

if __name__ == "__main__":
    main()    
    
    