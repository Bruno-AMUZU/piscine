#   
#   
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#

print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste = []
commande = ''

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        personne = input("Qui nage ? ")
        nage = input("quelle nage ? ")
        longueur = input("combien de longueur ? ")
        date = input("Quel jour ? YY_MM_DD")
        liste.append((personne,nage,longueur,date))
   
    if commande == 'liste':
        for elt in liste:
            print(f"Prénom {elt[0]}, nage {elt[1]}, longueur {elt[2]},Date {elt[3]}")

    if commande == 'nage':
        n=input("Quelle nage ?")
        for elt in liste:
            if elt[1] == n:
                print(f"Prénom:{elt[0]},longueur {elt[2]},Date {elt[3]}")

    if commande == 'nageur':
        na = input("Qui?")
        for elt in liste:
            if elt[0] == na:
                print(f"Nage: {elt[1]}")

    if commande == 'date':
        da=input("Quelle date?")
        for elt in list:
            if elt[3] == da:
                print(f"Prénom {elt[0]},nage {elt[1]},")