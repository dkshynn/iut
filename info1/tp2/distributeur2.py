somme = int(input("Saisie somme en Euro : "))
resultat = f"{somme} = "
c_inter = 0

if somme // 500 > 0 :
    c_inter = somme // 500
    resultat += f"{c_inter} * 500"
    somme %= 500
    if somme > 0 :
        resultat += " + "

if somme // 200 > 0 :
    c_inter = somme // 200
    resultat += f"{c_inter} * 200"
    somme %= 200
    if somme > 0 :
        resultat += " + "

if somme // 100 > 0 :
    c_inter = somme // 100
    resultat += f"{c_inter} * 100"
    somme %= 100
    if somme > 0 :
        resultat += " + "

if somme // 50 > 0 :
    c_inter = somme // 50
    resultat += f"{c_inter} * 50"
    somme %= 50
    if somme > 0 :
        resultat += " + "

if somme // 20 > 0 :
    c_inter = somme // 20
    resultat += f"{c_inter} * 20"
    somme %= 20
    if somme > 0 :
        resultat += " + "

if somme // 10 > 0 :
    c_inter = somme // 10
    resultat += f"{c_inter} * 10"
    somme %= 10
    if somme > 0 :
        resultat += " + "

if somme // 5 > 0 :
    c_inter = somme // 5
    resultat += f"{c_inter} * 5"
    somme %= 5
    if somme > 0 :
        resultat += " + "

if somme // 2 > 0 :
    c_inter = somme // 2
    resultat += f"{c_inter} * 2"
    somme %= 2
    if somme > 0 :
        resultat += " + "

if somme // 1 > 0 :
    c_inter = somme // 1
    resultat += f"{c_inter} * 1"

print(f"{resultat} €")

