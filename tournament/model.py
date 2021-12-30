class Tournament:
    def __init__(self):
        self.name = str
        self.description = str
        self.nb_rounds = 4
        self.default_max_players = 8
        self.timer = "Bullet"
        self.location = str
        self.players_list = list
        self.current_match_players_list = list
        self.match_list = list

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_nb_rounds(self):
        return self.nb_rounds

    def set_nb_rounds(self, nb_rounds):
        self.nb_rounds = nb_rounds

    def get_default_max_players(self):
        return self.default_max_players

    def set_default_max_players(self, default_max_players):
        self.default_max_players = default_max_players

    def get_timer(self):
        return self.timer

    def set_timer(self, timer):
        self.timer = timer

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_players_list(self):
        return self.players_list

    def set_players_list(self, players_list):
        self.players_list = players_list

    def get_current_match_players_list(self):
        return self.current_match_players_list

    def set_current_match_players_list(self, current_match_players_list):
        self.current_match_players_list = current_match_players_list

    def get_match_list(self):
        return self.match_list

    def set_match_list(self, match_list):
        self.match_list = match_list

