#DEBUT
#On admet que la fonction random existe et renvoie un chiffre aléatoire entre 0 et 2
from random import randint
#On admet que la fonction input existe et demander à l'utilisateur une chaine de caractère et la retourne
#Définir la variable pseudo à laquelle est associé le retour d'execution de la fonction input
pseudo = input("Entrer votre pseudo")
#Définir la fonction rpsMiniGame qui contient le mini-jeu
def rpsMiniGame (scoreJoueur= 0, scoreIa= 0, tieGame=0 ):
    #Definir une liste coups [pierre, feuille, ciseaux]
    listeCoups= ["pierre","feuille","ciseaux"]
    coupCorrect = False
    while coupCorrect == False :
        try:
                #Définir la variable choixJoueur qui prend l'index d'un élément de la liste coup en fonction de l'input du joueur.
                choixJoueur= listeCoups[int(input("Choissiser 0 pour pierre, 1 pour feuille ou 2 pour ciseaux"))]
                break
        except IndexError:
                print("Le choix n'est pas correcte, veuillez entrer un chiffre entre 0 et 2")
    #Définir la variable choixIa à laquelle est associé le retour d'execution de la fonction random
    choixIa= listeCoups[randint(0,2)]
    #Si choixJoueur égale pierre et si choixIa égale ciseaux
    if choixJoueur == "pierre" and choixIa == "ciseaux" :
        #Alors afficher le message "Bravo, vous avez gagnez la manche"
        print("Bravo, vous avez gagnez la manche")
        #Alors incrémenter  de 1 à scoreJoueur
        scoreJoueur = scoreJoueur + 1
        #Afficher scoreJoueur
        print(pseudo, scoreJoueur)
        #Afficher scoreIa
        print("IA", scoreIa)
    #Sinon si choixJoueur égale pierre et si choixIa égale feuille
    elif choixJoueur == "pierre" and choixIa == "feuille" :
            #Alors afficher le message "Dommage, vous avez perdu la manche"
            print("Dommage, vous avez perdu la manche")
            #Alors incrémenter de 1 à scoreIa
            scoreIa = scoreIa + 1
            #Afficher scoreJoueur
            print(pseudo, scoreJoueur)
            #Afficher scoreIa
            print("IA", scoreIa)
    #Sinon si choixJoueur égale pierre et si choixIa égale pierre
    elif choixJoueur == "pierre" and choixIa == "pierre" :
            #Alors afficher le message "C'est une égalité!"
            print("C'est une égalité!")
            #Alors incrémenter de 1 à tieGame
            tieGame = tieGame + 1
            #Afficher scoreJoueur
            print(pseudo, scoreJoueur)
            #Afficher scoreIa
            print("IA", scoreIa)

    #Sinom si choixJoueur égale feuille et si choixIa égale pierre
    elif choixJoueur == "feuille" and choixIa == "pierre" :
            #Alors afficher le message "Bravo, vous avez gagnez la manche"
            print("Bravo, vous avez gagnez la manche")
            #Alors incrémenter de 1 à scoreJoueur
            scoreJoueur = scoreJoueur + 1
            #Afficher scoreJoueur
            print(pseudo, scoreJoueur)
            #Afficher scoreIa
            print("IA", scoreIa)
    #Sinon si choixJoueur égale feuille et si choixIa égale ciseaux
    elif choixJoueur == "feuille" and choixIa == "ciseaux" :
            #Alors afficher le message "Dommage, vous avez perdu la manche"
            print("Dommage, vous avez perdu la manche")
            #Alors incrémenter de 1 à scoreIa
            scoreIa = scoreIa + 1
            #Afficher scoreJoueur
            print(pseudo, scoreJoueur)
            #Afficher scoreIa
            print("IA", scoreIa)
    #Sinon si choixJoueur égale feuille et si choixIa égale feuille
    elif choixJoueur == "feuille" and choixIa == "feuille" :
            #Alors afficher le message "C'est une égalité!"
            print("C'est une égalité!")
            #Alors incrémenter de 1 à tieGame
            tieGame = tieGame + 1
            #Afficher scoreJoueur
            print(pseudo, scoreJoueur)
            #Afficher scoreIa
            print("IA", scoreIa)

    #Sinon si choixJoueur égale ciseaux et si choixIa égale feuille
    elif choixJoueur == "ciseaux" and choixIa == "feuille" :
            #Alors afficher le message "Bravo, vous avez gagnez la manche"
            print("Bravo, vous avez gagnez la manche")
            #Alors incrémenter de 1 à scoreJoueur
            scoreJoueur = scoreJoueur + 1
            #Afficher scoreJoueur
            print(pseudo, scoreJoueur)
            #Afficher scoreIa
            print("IA", scoreIa)
    #Sinon si choixJoueur égale ciseaux et si choixIa égale Pierre
    elif choixJoueur == "ciseaux" and choixIa == "pierre" :
            #Alors afficher le message "Dommage, vous avez perdu la manche"
            print("Dommage, vous avez perdu la manche")
            #Alors incrémenter de 1 à scoreIa
            scoreIa = scoreIa + 1
            #Afficher scoreJoueur
            print(pseudo, scoreJoueur)
            #Afficher scoreIa
            print("IA", scoreIa)
    #Sinon si choixJoueur égale ciseaux et si choixIa égale ciseaux
    elif choixJoueur == "ciseaux" and choixIa == "ciseaux" :
            #Alors afficher le message "C'est une égalité!"
            print("C'est une égalité!")
            #Alors incrémenter de 1 à tieGame
            tieGame = tieGame + 1
            #Afficher scoreJoueur
            print(pseudo, scoreJoueur)
            #Afficher scoreIa
            print("IA", scoreIa)
    #Sinon le choix n'est pas correcte
    else :
        #Alors afficher "Le choix n'est pas correcte"
        print("Votre choix n'est pas correcte")
        rpsMiniGame()

    
    #Si scoreJoueur égale à 3
    if scoreJoueur == 3 :
        #Retourner
            #Afficher "Félicitation, vous avez battu le bot. Vous faites partie de l'ELITE de la nation"
            print("Félicitation, vous   avez battu le bot. Vous faites partie de l'ELITE de la nation")
            #scoreJoueur
            print("Votre score est de" ,scoreJoueur)
            #scoreIa
            print("Le score de l'IA est de", scoreIa)
            #tieGame
            print("Vous avez fait", tieGame, "égalité(s)")
    #Sinon si scoreIa égale à 3
    elif scoreIa == 3 :
        #Retourner  
            #Afficher "Vous n'avez pas pu battre un simple bot, retourner à l'entrainement"
            print("Vous n'avez pas pu battre un simple bot, retourner à l'entrainement")
            #scoreJoueur
            print("Votre score est de" ,scoreJoueur)
            #scoreIa
            print("Le score de l'IA est de", scoreIa)
            #tieGame
            print("Vous avez fait", tieGame, "égalité(s)")
    else :
        rpsMiniGame(scoreJoueur, scoreIa, tieGame)
    #Fin du mini-jeu
#Executer la fonction rpsMiniGame
rpsMiniGame()
#FIN