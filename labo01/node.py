class Node:
    """
        Creation du node qui permetra de cree des listes et de les linker ensemble.
    """
    def __init__(self, data, next):
        """
            Initialise les attributs data et next.
            :param data: le data a etre ajouter
            :param next: pointeur du prochain node
        """
        self.data = data
        self.next = next

    def __str__(self):
        """
            :return: retourne le node en format string
        """
        return f"{self.data}\n"
