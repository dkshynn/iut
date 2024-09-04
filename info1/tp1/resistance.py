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

userColor1 = input("Entrez la couleur de la première bande: ")
userColor2 = input("Entrez la couleur de la deuxième bande: ")
userColor3 = input("Entrez la couleur de la troisième bande: ")


resistance = ((dictionnaire[userColor1] * 10 ) + dictionnaire[userColor2])*(10**dictionnaire[userColor3])
print(resistance)