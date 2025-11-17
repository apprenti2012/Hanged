import random
reset=True
while reset==True:
    
    choix = input("Mode de jeu : solo ou deux joueurs (1 ou 2): ")
    if choix =="2" :
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
       -|   |
            |
            |
        =========
        """,
        """
        -----
        |   |
        O   |
       -|-  |
            |
            |
        =========
        """,
        """
        -----
        |   |
        O   |
       -|-  |
       |    |
            |
        =========
        """,
        """
        -----
        |   |
        O   |
       -|-  |
       | |  |
            |
        =========
        """
        ]

        while True:
            print(pendu[erreurs])
            print("\nMot à deviner :", " ".join(affichage))
            print("Lettres déjà essayées :", ", ".join(lettres_devinees))
            print(f"Erreurs : {erreurs}/{max_erreurs}")

            lettre = input("Devine une lettre : ").lower()

            if lettre in lettres_devinees:
                print("Tu as déjà essayé cette lettre !\n")
                continue

            lettres_devinees.append(lettre)

            if lettre in mot:
                for i, l in enumerate(mot):
                    if l == lettre:
                        affichage[i] = lettre
                print("Bien joué !\n")
            else:
                erreurs += 1
                print("Mauvaise lettre...\n")

            if "_" not in affichage:
                print("\nFélicitations ! Tu as trouvé le mot :", mot)
                break
            if erreurs >= max_erreurs:
                print(pendu[erreurs])
                print("\nPerdu ! Le mot était :", mot)
                break
        recommencé=input("Veux tu recommencé ? :")
        if recommencé=="oui":
            reset=True
        else:
            reset=False    
    elif choix=="1" :
        mots= [
        "ordinateur",
        "python",
        "voiture",
        "maison",
        "chocolat",
        "soleil",
        "panda",
        "bouteille",
        "hiver",
        "fantome",
        "ecole",
        "fromage",
        "pirate",
        "dragon",
        "licorne",
        "mystere",
        "salade",
        "banane",
        "valise",
        "montagne"
        ]
        mot=random.choice(mots)
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
       -|   |
            |
            |
        =========
        """,
        """
        -----
        |   |
        O   |
       -|-  |
            |
            |
        =========
        """,
        """
        -----
        |   |
        O   |
       -|-  |
       |    |
            |
        =========
        """,
        """
        -----
        |   |
        O   |
       -|-  |
       | |  |
            |
        =========
        """
        ]

        while True:
            print(pendu[erreurs])
            print("\nMot à deviner :", " ".join(affichage))
            print("Lettres déjà essayées :", ", ".join(lettres_devinees))
            print(f"Erreurs : {erreurs}/{max_erreurs}")

            lettre = input("Devine une lettre : ").lower()

            if lettre in lettres_devinees:
                print("Tu as déjà essayé cette lettre !\n")
                continue

            lettres_devinees.append(lettre)

            if lettre in mot:
                for i, l in enumerate(mot):
                    if l == lettre:
                        affichage[i] = lettre
                print("Bien joué !\n")
            else:
                erreurs += 1
                print("Mauvaise lettre...\n")

            if "_" not in affichage:
                print("\nFélicitations ! Tu as trouvé le mot :", mot)
                break
            if erreurs >= max_erreurs:
                print(pendu[erreurs])
                print("\nPerdu ! Le mot était :", mot)
                break
        recommencé=input("Veux tu recommencé ? : ")
        if recommencé=="oui":
            reset=True
        else:
            reset=False    
    else:
        print("tu n'as pas tapé 1 ou 2, recommence")

