seconde = int(input("Entrez les secondes : "))
mois = input("Entrez le mois : ")

moisAnnee = {
    "janvier": 31,
    "fevrier": 28,
    "mars": 31,
    "avril": 30,
    "mai": 31,
    "juin": 30,
    "juillet": 31,
    "aout": 31,
    "septembre": 30,
    "octobre": 31,
    "novembre": 30,
    "decembre": 31
}
if moisAnnee[mois] == 31:
    moisSeconde = 2678400
elif moisAnnee[mois] == 30:
    moisSeconde = 2592000
elif moisAnnee[mois] == 28:
    moisSeconde = 2419200
else :
    print("erreur")


resultat = f"{seconde} s = "
c_inter = 0

if seconde // 31536000 : 
    c_inter = seconde // 31536000
    resultat += f"{c_inter} année(s)"
    seconde %= 31536000
    if seconde > 0 :
        resultat += " + "

if seconde // moisSeconde: 
    c_inter = seconde // moisSeconde
    resultat = f"{c_inter} mois"
    seconde %= moisSeconde
    if seconde > 0 :
        resultat += " + "

if seconde // 86400 : 
    c_inter += seconde // 86400
    resultat += f"{c_inter} jours"
    seconde %= 86400
    if seconde > 0 :
        resultat += " + "

if seconde // 3600 : 
    c_inter = seconde // 3600
    resultat += f"{c_inter} h"
    seconde %= 3600
    if seconde > 0 :
        resultat += " + "

if seconde // 60 : 
    c_inter = seconde // 60
    resultat += f"{c_inter} min"
    seconde %= 60
    if seconde > 0 :
        resultat += " + "

if seconde // 1 :
    c_inter = seconde // 1
    resultat += f"{c_inter} s"

print(resultat)

    