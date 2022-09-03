import random

movies = [
"13 lives",
"Around the World in 80 Days",
"Bro Daddy",
"Picket 43",
"Swapnakoodu",
"Cuttputlli",
"Vezham",
"Mike",
"Solomante Theneechakal",
"Sita Ramam"
]

print("Total number of movies: ", len(movies))

while True:
    print("Watch: ", random.choice(movies))
    if input("close? : ") == 'y':
        break