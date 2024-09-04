dictionnaire = {
    "N": 0,
    "M": 1,
    "R": 2,
    "O": 3,
    "J": 4,
    "V": 5,
    "B": 6,
    "P": 7,
    "G": 8,
    "W": 9
}

userColor0 = input("Saisissez vos 3 couleurs :")

if len(userColor0)>=3 :
    userColor1 = userColor0[0]
    userColor2 = userColor0[1]
    userColor3 = userColor0[2]

resistance = ((dictionnaire[userColor1] * 10 ) + dictionnaire[userColor2])*(10**dictionnaire[userColor3])
print(resistance)
