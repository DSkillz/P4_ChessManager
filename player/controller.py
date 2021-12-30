from player.view import ViewPlayer
from player.model import Player
from player.model import MethodPlayer
from tournament.controller import TournamentController


class MenuPlayer:
    def menu_add_player(self):
        """management menu addition players"""
        viewplayer = ViewPlayer()
        player = Player()
        player.name = input("Entrez un nom: ")
        player.first_name = input("Entrez un prénom: ")
        player.birth_date = input("Entrez une date de naissance (format, JJ/MM/AAAA): ")
        player.sex = input("Entrez un genre (H/F): ")
        # tournament = TournamentController().elements_player()
        cplayer = Player(**player)
        add_player = cplayer.add_players(player)
        resultat = MethodPlayer().duplicate_search(add_player)
        serialized_player = resultat.get("valided")
        existing = resultat.get("no_valided")
        if not serialized_player == []:
            cplayer.save_player(serialized_player)
            viewplayer.print_new_player_register()
            self.ask_add_again_player()
        if not existing == []:
            viewplayer.print_existing_player(existing)
            self.ask_add_again_player()

    def menu_modif_player(self):
        pass

    def modify_classement(self):
        pass

    def ask_add_again_player(self):
        pass

