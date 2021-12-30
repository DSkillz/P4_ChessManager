class MenuPlayer:
    def __init__(self, name, first_name, birth_date, sex, ranking=0, pk=None):
        self.pk = name + "_" + first_name + "_" + birth_date[-4:]
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.ranking = ranking


class MethodPlayer:
    pass



