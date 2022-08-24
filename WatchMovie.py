import random

movies = [
"13 lives",
"Around the World in 80 Days",
"Bro Daddy",
"Mike",
"Picket 43",
"Shamshera",
"Sita Ramam",
"Solomante Theneechakal",
"Swapnakoodu",
"Virus",
"Naku Penta Naku Taka",
"Ee Thanutha Veluppan Kalathu",
"Aadu",
"Utharam"
]

print("Total number of movies: ", len(movies))

while True:
    print("Watch: ", random.choice(movies))
    if input("close: ") == 'y':
        break