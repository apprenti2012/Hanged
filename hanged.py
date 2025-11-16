mot = input("Écris le mot à deviner : ").lower()
print("\n" * 50)

affichage = ["_"] * len(mot)
erreurs = 0
lettres_devinees = []
max_erreurs = 6

pendu = [
"""
 -----
 |   |
     |
     |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\  |
     |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\  |
/    |
     |
=========
""",
"""
 -----
 |   |
 O   |
/|\  |
/ \  |
     |
=========
"""
]

# Boucle principale
while True:
    # Afficher le pendu et l’état du mot
    print(pendu[erreurs])
    print("\nMot à deviner :", " ".join(affichage))
    print("Lettres déjà essayées :", ", ".join(lettres_devinees))
    print(f"Erreurs : {erreurs}/{max_erreurs}")

    # Demander une lettre
    lettre = input("Devine une lettre : ").lower()

    # Vérifier si la lettre a déjà été essayée
    if lettre in lettres_devinees:
        print("Tu as déjà essayé cette lettre !\n")
        continue

    lettres_devinees.append(lettre)

    # Vérifier si la lettre est dans le mot
    if lettre in mot:
        for i, l in enumerate(mot):
            if l == lettre:
                affichage[i] = lettre
        print("Bien joué !\n")
    else:
        erreurs += 1
        print("Mauvaise lettre...\n")

    # Vérifier conditions de victoire/défaite
    if "_" not in affichage:
        print("\nFélicitations ! Tu as trouvé le mot :", mot)
        break
    if erreurs >= max_erreurs:
        print(pendu[erreurs])
        print("\nPerdu ! Le mot était :", mot)
        break


