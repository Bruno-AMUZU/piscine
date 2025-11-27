#
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#

print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste = []
commande = ''
# MT COMMENTAIRE
while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        a = input("Qui nage ? ")
        b = input("quelle nage ? ")
        c = input("combien de longueur ? ")
        liste.append((a,b,c))

    if commande == 'nage':
        nage = input("quelle nage ? ")
        for elt in liste:
            if elt[1]== nage:
                print(f"Prénom {elt[0]}, longueur {elt[2]}")
   
    if commande == 'liste':
        for elt in liste:
            print(f"Prénom {elt[0]}, nage {elt[1]}, longueur {elt[2]}")

# Fin du programme
