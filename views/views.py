class ViewMenu:
    def __init__(self):
        pass

    def print_accueil(self):
        # menu printing and retrieval of menu choice

        print()
        print("Bienvenue sur le gestionnaire de jeu d'échec.\n")
        print("Selectionnez le menu souhaité.\n")
        print(" 1 : ajouter un joueur.")
        print(" 2 : modifier un joueur.")
        print(" 3 : création d'un tournoi.")
        print(" 4 : jouer un tournoi créé.")
        print(" 5 : classement.")
        print(" 6 : modification du classement.")
        print(" 7 : rapport.")
        print(" 8 : sortir du logiciel.")
        print("\nQuel est votre choix : ")
        resultat = input()
        return resultat

    def print_choice_input_menu(self, resultat):
        pass

    def print_error_enter_int(self, ve):
        print(f'Vous avez entré {ve}, recommenceez svp.')
