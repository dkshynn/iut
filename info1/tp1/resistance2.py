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
else : 
    print('erreur')

if userColor1 in dictionnaire and userColor2 in dictionnaire and userColor3 in dictionnaire :
    resistance = ((dictionnaire[userColor1] * 10 ) + dictionnaire[userColor2])*(10**dictionnaire[userColor3])
else : 
    print("erreur2")

if resistance>=1000 and resistance<1000000:
    resistanceK = resistance/1000
    print(resistanceK, "Kohm")
elif resistance>=1000000:
    resistanceM = resistance/1000000
    print(resistanceM, "Mohm")
else :
    print(resistance, "ohm")

