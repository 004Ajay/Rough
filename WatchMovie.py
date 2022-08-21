import random

movies = [
"13 lives",
"Around the World in 80 Days",
"Bro Daddy",
"dejavu",
"Heaven",
"mike",
"nna than case kodu",
"Picket 43",
"shamshera",
"sita ramam",
"Solomante Theneechakal",
"swapnakoodu",
"Thallumala",
"varayan",
"virus"
]

while True:
    print("Watch: ", random.choice(movies))
    if input("close: ") == 'y':
        break