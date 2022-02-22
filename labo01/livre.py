JOURS_MAX = 7


class Livre:
    def __init__(self):
        """
        Initialise les deux attributs de la class Libre
        (deja_reserver) si le livre est reserver retourne False
        (jour_reserver) le jour reserver retourne None
        """
        self.deja_reserver = False
        self.jour_reserver = None

    def jour_restant(self, date: int) -> int:
        """
        Donne le nombre de jours restant a la reservation d'un livre
        :param date: un jour
        :return: nombre de jour restant
        """
        return JOURS_MAX - (date - self.jour_reserver)

    def __str__(self):
        """
        :return: Retourne un string de l'objet Livre
        """
        return f"Livre reserver: {self.deja_reserver} Nombre de jours: {self.jour_reserver}"
