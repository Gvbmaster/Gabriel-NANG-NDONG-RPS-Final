#DEBUT
#On admet que la fonction random existe et renvoie un chiffre aléatoire entre 0 et 2
#On admet que la fonction input existe et demander à l'utilisateur une chaine de caractère et la retourne
#Définir la fonction RPSMiniGame qui contient le mini-jeu
    #On associe à pseudo le retour d'execution de la fonction input
    #Definir une liste coups [pierre, feuille, ciseaux]
    #Définir la variable choixJoueur qui prend l'index d'un élément de la liste coup en fonction de l'input du joueur.
    #Définir la variable choixIa à laquelle est associé le retour d'execution de la fonction random 
    #Définir la variable scoreJoueur associé à 0
    #Définir la variable scoreIa associé à 0
    #Définir la variable tieGame associé à 0
    #Si choixJoueur égale pierre et si choixIa égale ciseaux
        #Alors afficher le message "Bravo, vous avez gagnez la manche"
        #Alors incrémenter  de 1 à scoreJoueur
        #Afficher scoreJoueur
        #Afficher scoreIa
        #Sinon si choixJoueur égale pierre et si choixIa égale feuille
            #Alors afficher le message "Dommage, vous avez perdu la manche"
            #Alors incrémenter de 1 à scoreIa
            #Afficher scoreJoueur
            #Afficher scoreIa
        #Sinon si choixJoueur égale pierre et si choixIa égale pierre
            #Alors afficher le message "C'est une égalité!"
            #Alors incrémenter de 1 à tieGame
            #Afficher scoreJoueur
            #Afficher scoreIa
        
        #Si choixJoueur égale feuille et si choixIa égale pierre
            #Alors afficher le message "Bravo, vous avez gagnez la manche"
            #Alors incrémenter de 1 à scoreJoueur
            #Afficher scoreJoueur
            #Afficher scoreIa
        #Sinon si choixJoueur égale feuille et si choixIa égale ciseaux
            #Alors afficher le message "Dommage, vous avez perdu la manche"
            #Alors incrémenter de 1 à scoreIa
            #Afficher scoreJoueur
            #Afficher scoreIa
        #Sinon si choixJoueur égale feuille et si choixIa égale feuille
            #Alors afficher le message "C'est une égalité!"
            #Alors incrémenter de 1 à tieGame
            #Afficher scoreJoueur
            #Afficher scoreIa

        #Si choixJoueur égale ciseaux et si choixIa égale feuille
            #Alors afficher le message "Bravo, vous avez gagnez la manche"
            #Alors incrémenter de 1 à scoreJoueur
            #Afficher scoreJoueur
            #Afficher scoreIa
        #Sinon si choixJoueur égale ciseaux et si choixIa égale Pierre
            #Alors afficher le message "Dommage, vous avez perdu la manche"
            #Alors incrémenter de 1 à scoreIa
            #Afficher scoreJoueur
            #Afficher scoreIa
        #Sinon si choixJoueur égale ciseaux et si choixIa égale ciseaux
            #Alors afficher le message "C'est une égalité!"
            #Alors incrémenter de 1 à tieGame
            #Afficher scoreJoueur
            #Afficher scoreIa
    #Sinon le choix n'est pas correcte
        #Alors afficher "Le choix n'est pas correcte"
    
    #Si scoreJoueur égale à 3
        #Retourner
            #Afficher "Félicitation, vous avez battu le bot. Vous faites partie de l'ELITE de la nation"
            #scoreJoueur
            #scoreIa
            #tieGame
    #Sinon si scoreIa égale à 3
        #Retourner 
            #Afficher "Vous n'avez pas pu battre un simple bot, retourner à l'entrainement"
            #scoreJoueur
            #scoreIa
            #tieGame
    #Fin du mini-jeu
#Executer la fonction RPSMiniGame
#FIN