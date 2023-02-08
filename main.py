with open("names.txt", "r") as file:
    name_list = file.read().split()

# Les imports toujours en début de fichier
import random

random_name_1 = random.choice(name_list)
# Ici au lieu d'enchaîner les deux randoms tu peux retirer le random_name_1 de la name_list
# Comme ça t'es sûr que le random_name_2 ne sera jamais le même que le 1, et t'auras pas besoin
# de faire de condition plus bas
# Si jamais t'as besoin que ta name_list ne change pas (ce qui sera sûrement le cas),
# tu peux la copier et tout faire sur la copie (random.choices, retrait du nom)
# Genre si tu veux permettre le choix plusieurs fois de suite, tu peux faire une boucle
# et à chaque début de boucle tu créées une copie temporaire de la name_list pour tout faire dessus
random_name_2 = random.choice(name_list)

left_hero = random_name_1
left_wins = 0
left_loses = 0

right_hero = random_name_2
right_wins = 0
right_loses = 0

user_okay = True



if left_hero == right_hero:
    exit()
    # en realité s'ils sont égaux on relance le choix random du right_hero
else:
    # J'aurais appelé le booléen "choice_okay" au lieu de "user_okay" pour plus de clareté
    # Inverser la condition serait aussi plus clair. Là je lis "tant que c'est okay on recommence,
    # et quand c'est plus okay on arrête", alors que c'est l'inverse.
    while user_okay == True:
        user_choice = input(f"Tapez 1 si vous votez pour {left_hero}, ou 2 si vous votez pour {right_hero}.")
        if user_choice == "1":
            left_wins += 1
            right_loses += 1
            print(f"Vous avez voté pour {left_hero} !")
            user_okay = False
        elif user_choice == "2":
            right_wins += 1
            left_loses += 1
            print(f"Vous avez voté pour {right_hero} !")
            user_okay = False
        else:
            print("Merci de taper uniquement 1 ou 2, espèce de gros naze.")
            user_okay = True
        