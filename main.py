from controller import MainMenu


def start_programme():
    if __name__ == "__main__":
        MainMenu().menu()


start_programme()


# Grossièrement:
# - les print et messages sont dans les vues
# - les input et la mise à jour de tes modèles sont dans les contrôleurs
# - la logique métier est centrée dans les modèles (récupération des scores, d'un tour de tournoi, update, création, etc.).
# Ce sont aussi les modèles qui dialoguent directement avec la base de données.
# En terme de dépendances:
# - les modèles n'ont accès à rien (mis à part d'autres modèles)
# - les vues peuvent accéder aux modèles
# - les contrôleurs ont accès aux vues et aux modèles, et gèrent le fonctionnement de l'application

# Dans l'idéal, les contrôleurs donnent juste ce qu'il faut de modèle aux vues. Les vues se servent de modèles seulement pour afficher des données.
