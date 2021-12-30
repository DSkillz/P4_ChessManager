class Player:
    def __init__(self, name="", first_name="", birth_date="", sex="", rank=0, pk=None):
        self.pk = name + "_" + first_name + "_" + birth_date[-4:]
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank

    def add_players(self):
        pass

    def save_player(self):
        pass


class MethodPlayer:
    def duplicate_search(self):
        pass

    def rank_stats(self):
        pass



