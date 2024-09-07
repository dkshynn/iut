somme = int(input("Saisie somme en Euro :"))

user = f"{somme} = "

if somme/500 <= somme/200 and somme/500>=1: 
    if somme % 500 == 0 :
        user = user + f"{int(somme/500)}* 500"
        print(f"{user}")
    elif somme/200 <= 100 and somme/200>=1:
        if (somme-int(somme/500)*500) % 200 == 0 :
            print(f"{somme} = {int(somme/500)} * 500 + {int((somme%500)/200)} * 200")
            user = user + f"+{int(somme/500)} * 500 + {int((somme%500)/200)} * 200"
            if somme/20 <= 10 and somme/20>=1:
                user = user + f" + {int((somme-(int(somme/500)*500)-(int((somme%500)/20)*20))/20)} * 20"
                print(f"{user}")
                """ if somme/5 <= 2 and somme/5>=1:
                    user = user + f" + {}" """
        

    """ elif somme/200 <= 100 and somme/200>=1:
    elif somme/100 <= 50 and somme/100>=1:
    elif somme/50 <= 20 and somme/50>=1:
    elif somme/20 <= 10 and somme/20>=1:
    elif somme/10 <= 5 and somme/10>=1:
    elif somme/5 <= 2 and somme/5>=1:
    elif somme/2 <= 1 and somme/2>=1:
    elif somme>=1 and somme%1>=1: """
else:
    print("error")


