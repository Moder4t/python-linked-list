from linkedlist import LinkedList, Node
from livre import Livre


class Library:
    """
        Permet au client de louer un livre pour une periode de 7 jours
    """
    def __init__(self):
        """
        Initialise l'attribut de la class Library
        (livre) la liste des livre disponible
        """
        self.livres: LinkedList = LinkedList()
        for livre in range(10):
            self.livres.ajout_premier(Livre())

    def verification_livre(self, index: int) -> Livre:
        """
        choisir un livre par sa valeur dans l'index
        :param index: position original du livre
        :return: pointeur du livre
        """
        return self.livres.position(index)

    def reservation_de_livre(self, client: int, index: int, date: int):
        """
        Reserve un livre pour 7 jours
        :param client: index des clients pour la journee
        :param index: indes des livres a reserver
        :param date: jour de la reservation
        :return: None
        """

        livre: Livre = self.verification_livre(index)
        if livre.deja_reserver:

            jours: int = livre.jour_restant(date)
            raise Exception(
                f"Cher client {client}, le livre {index} n'est plus disponible, il le sera dans {jours} jour(s)"
            )

        livre.deja_reserver = True
        livre.jour_reserver = date

    def retour_de_livre(self, date: int):
        """
        Retour des livres reserver apres 7 jours ecouler
        :param date: jour de retour
        :return: None
        """
        node: Node = self.livres.head
        while node is not None:
            livre: Livre = node.data
            if livre.deja_reserver and livre.jour_restant(date) == 0:
                livre.deja_reserver = False
                livre.jour_reserver = None
            node = node.next

    def __str__(self):
        return str(self.livres)
