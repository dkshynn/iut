if n_seconde // 60 : 
    c_inter = n_seconde // 60
    resultat = f"{c_inter} min"
    n_seconde %= 60
    if n_seconde > 0 :
        resultat += " + "

if n_seconde // 1 :
    c_inter = n_seconde // 1
    resultat = f"{c_inter} s"