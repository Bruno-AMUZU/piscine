#   
#   
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#

print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste_nageurs = ["Pierre", "Léa", "Michel"]

liste_nages = ["brasse","crawl","Dos"]

liste_bdd = [(1,0,15,"25-11-24"),
        (0,0,9,"25-11-24"),
        (2,1,8,"25-11-26"),
        (1,1,10,"25-11-25"),
        (0,2,9,"25-11-26"),
        (2,0,9,"25-11-26")]
commande = ''

nom_fichier = 'utilisateur.txt'

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        print("Nageurs:")
        for id, nageur in enumerate(liste_nageurs):
            print(f"{id+1}->{nageur}")
        personne = int(input("Quel nageur est concerné ? ")) - 1
        for id, nage in enumerate(liste_nages):
            print(f"{id+1}->{nage}")
        nage = int(input("quelle nage ? "))- 1
        longueur = input("combien de longueur ? ")
        date = input("Quel jour ? YY_MM_DD")
        liste_bdd.append((personne,nage,longueur,date))
   
    if commande == 'liste':
        for personne, nage, longueur, date in liste_bdd:
            print(f"Prénom {liste_nageurs[personne]}, nage {liste_nages[nage]}, longueur {longueur},Date {date}")

    if commande == 'nage':
        print("Nages:")
        for id, nage in enumerate(liste_nages):
            print(f"{id+1}->{nage}")
        n=int(input("Quelle nage est concernée ? ")) - 1
        for personne, nage, longueur, date in liste_bdd:
            if nage == n:
                print(f"Prénom {liste_nageurs[personne]},longueur {longueur},Date {date}")

    if commande == 'nageur':
        print("Nageurs:")
        for id, nageur in enumerate(liste_nageurs):
            print(f"{id+1}->{nageur}")
        na = int(input("Quel nageur est concerné ? ")) - 1
        for personne, nage, longueur, date in liste_bdd:
            if personne == na:
                print(f"Nage {liste_nages[nage]},longueur {longueur},Date {date}")

    if commande == 'date':
        da=input("Quelle date?")
        for personne, nage, longueur, date in liste_bdd:
            if date == da:
                print(f"Prénom {liste_nageurs[personne]},nage {liste_nages[nage]},longueur {longueur}")

    if commande == 'save':
        with open(nom_fichier, 'w',  encoding='utf-8') as f:
                f.write("@nageurs\n")
                for id, nom in enumerate(liste_nageurs):
                    f.write(f"{id}, {nom}\n")
                f.write("@nages\n")
                for id, nom in enumerate(liste_nages):
                    f.write(f"{id}, {nom}\n")
                f.write("@table")
                for personne, nage, longueur, date in liste_bdd:
                    f.write(f"{liste_nageurs[personne]},{liste_nages[nage]},{longueur},{date}\n")
        print(f"Liste sauvegardée ! dans '{nom_fichier}'.")

    if commande == 'load':
        liste_bdd.clear()
        liste_nages.clear()
        liste_nageurs.clear()
        l = liste_nageurs  # initialisation ne sert aps de suite
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            for line in fichier:
                if line[0]=='@':
                    if line[1:]=='nage':
                        # j'ai découvert que je lis la table des nages
                        l = liste_nages
                    if line[1:]=='nageurs':
                        # j'ai découvert que je lis la table des nages
                        l = liste_nageurs
                    if line[1:]=='table':
                        # j'ai découvert que je lis la table des nages
                        l = liste_bdd
                else:
                    valeurs = [v.strip() for v in line.split(',')]
                    if l == liste_nages:
                        liste_nages.append(valeurs[1])
                    if l == liste_nageurs:
                        liste_nages.append(valeurs[1])
                    if l == liste_bdd:
                        liste_nages.append((valeurs[0],valeurs[1],valeurs[2],valeurs[3]) )