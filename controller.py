import sys

from player.controller import MenuPlayer
from player.model import MethodPlayer
from tournament.controller import MenuTournament
from tournament.model import Tournament
from views.views import ViewMenu


class MainMenu:

    def menu(self):
        # menu distribution function

        menuplayer = MenuPlayer()
        viewmenu = ViewMenu()
        result = viewmenu.print_accueil()
        tournament = Tournament()
        # try:
        viewmenu.print_choice_input_menu(result)
        # except ValueError:
        #     viewmenu.print_error_enter_int()
            # self.menu()

        if result == "1":  # adding player
            menuplayer.menu_add_player()
            # self.menu()
        elif result == "2":  # player modification
            menuplayer.menu_modif_player()
            # self.menu()
        elif result == "3":  # creation of a tournament
            turn = 1
            MenuTournament().play_tournament(turn)
            # self.menu()
        elif result == "4":  # to see all tournaments created and play tournaments not finalized
            MethodMainMenu().find_and_play_tournament()
            # self.menu()
        elif result == "5":  # see the ranking
            retour_list = MethodPlayer().rank_stats()
            player_sort_ranking = retour_list[0]
            viewmenu.print_rank(player_sort_ranking)
            # ViewToShare().print_pass_validation()
            # self.menu()
        elif result == "6":  # allows the modification of rank points per players
            menuplayer.modify_classement()
            # self.menu()
        elif result == "7":  # access to the report management menu
            MainMenu().menu_reports()
            # self.menu()
        elif result == "8":  # to exit the program
            sys.exit()
        # else:
        #     viewmenu.print_error_enter_int()
        #     self.menu()

    def menu_reports(self):
        pass

class MethodMainMenu:
    pass
