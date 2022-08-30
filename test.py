while reply != 'c':
    steps += 1 # incrementing step count
    guess = random.randint(start, stop) # computer guessing a random num
    reply = input(f'{guess}, low, high or correct (L, H, C)? : ').lower()
    if reply == 'h':
        stop = guess - 1
    elif reply == 'l':
        start = guess + 1
print(f'Computer correctly guessed, {guess}\nNumber of steps: {steps}')