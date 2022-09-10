import random

movies = [
"Around the World in 80 Days",
"Bro Daddy",
"Picket 43",
"Swapnakoodu",
"Mike",
"Solomante Theneechakal"
]

print("Total number of movies: ", len(movies))

while True:
    print("Watch: ", random.choice(movies))
    if input("close? : ") == 'y':
        break