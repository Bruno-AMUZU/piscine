#   
#   
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#

print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste = [("Léa","brasse",15,"25-11-24"),
        ("Pierre","brasse",9,"25-11-24"),
        ("Michel","crawl",8,"25-11-26"),
        ("Léa","crawl",10,"25-11-25"),
        ("Pierre","Dos",9,"25-11-26"),
        ("Michel","Brasse",9,"25-11-26")]
commande = ''

nom_fichier = 'utilisateur.txt'

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        personne = input("Qui nage ? ")
        nage = input("quelle nage ? ")
        longueur = input("combien de longueur ? ")
        date = input("Quel jour ? YY_MM_DD")
        liste.append((personne,nage,longueur,date))
   
    if commande == 'liste':
        for personne, nage, longueur, date in liste:
            print(f"Prénom {personne}, nage {nage}, longueur {longueur},Date {date}")

    if commande == 'nage':
        n=input("Quelle nage ?")
        for personne, nage, longueur, date in liste:
            if nage == n:
                print(f"Prénom {personne},longueur {longueur},Date {date}")

    if commande == 'nageur':
        na = input("Qui?")
        for personne, nage, longueur, date in liste:
            if personne == na:
                print(f"Nage {nage},longueur {longueur},Date {date}")

    if commande == 'date':
        da=input("Quelle date?")
        for personne, nage, longueur, date in liste:
            if date == da:
                print(f"Prénom {personne},nage {nage},longueur {longueur}")

    if commande == 'save':
  
        for elt in liste:
            with open(nom_fichier, 'w',  encoding='utf-8') as f:
                    for personne, nage, longueur, date in liste:
                        f.write(f"{personne},{nage},{longueur},{date}\n")
        print(f"Liste sauvegardée ! dans '{nom_fichier}'.")

    if commande == 'load':
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            for ligne in nom_fichier:
                ligne = ligne.strip()
                
                if ligne:
                    valeurs = [v.strip() for v in ligne.split(',')]
                    
                    prenom, nom, longueur_str, date = valeurs
                    longueur = int(longueur_str) 
                    
                    print(f"Prénom: {prenom}, Nom: {nom}, Longueur: {longueur}, Date: {date}")