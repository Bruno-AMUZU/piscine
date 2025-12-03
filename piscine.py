#   
#   
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#

print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste_nageurs = ["Pierre", "Léa", "Michel"]

liste_nages = []

liste_bdd = [(1,"brasse",15,"25-11-24"),
        (0,"brasse",9,"25-11-24"),
        (2,"crawl",8,"25-11-26"),
        (1,"crawl",10,"25-11-25"),
        (0,"Dos",9,"25-11-26"),
        (2,"Brasse",9,"25-11-26")]
commande = ''

nom_fichier = 'utilisateur.txt'

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        personne = input("Qui nage ? ")
        nage = input("quelle nage ? ")
        longueur = input("combien de longueur ? ")
        date = input("Quel jour ? YY_MM_DD")
        liste_bdd.append((personne,nage,longueur,date))
   
    if commande == 'liste':
        for personne, nage, longueur, date in liste_bdd:
            print(f"Prénom {liste_nageurs[personne]}, nage {liste_nages[nage]}, longueur {longueur},Date {date}")

    if commande == 'nage':
        n=input("Quelle nage ?")
        for personne, nage, longueur, date in liste_bdd:
            if nage == n:
                print(f"Prénom {liste_nageurs[personne]},longueur {longueur},Date {date}")

    if commande == 'nageur':
        na = input("Qui?")
        for personne, nage, longueur, date in liste_bdd:
            if personne == na:
                print(f"Nage {liste_nages[nage]},longueur {longueur},Date {date}")

    if commande == 'date':
        da=input("Quelle date?")
        for personne, nage, longueur, date in liste_bdd:
            if date == da:
                print(f"Prénom {liste_nageurs[personne]},nage {liste_nages[nage]},longueur {longueur}")

    if commande == 'save':
  
        for elt in liste_bdd:
            with open(nom_fichier, 'w',  encoding='utf-8') as f:
                    for personne, nage, longueur, date in liste_bdd:
                        f.write(f"{liste_nageurs[personne]},{liste_nages[nage]},{longueur},{date}\n")
        print(f"Liste sauvegardée ! dans '{nom_fichier}'.")

    if commande == 'load':
        liste_bdd.clear()
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                
                if ligne:
                    valeurs = [v.strip() for v in ligne.split(',')]
                    
                    prenom, nom, longueur_str, date = valeurs
                    longueur = int(longueur_str) 
                    
                    print(f"Prénom: {prenom}, Nom: {nom}, Longueur: {longueur}, Date: {date}")
                    liste_bdd.append((prenom,nom,longueur,date))