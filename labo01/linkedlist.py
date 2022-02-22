from node import Node


class LinkedList:
    """
        Creation d'une LinkedList
    """
    def __init__(self):
        self.head = None

    def ajout_premier(self, data):
        """
        ajoute le 1er element de la liste
        :param data: Data a etre inserer dans la liste
        :return: None
        The function updates both the head and the
        length attributes of the list
        """
        node = Node(data, self.head)
        self.head = node

    def ajout_dernier(self, data):
        """
        Ajoute le dernier element de la liste
        :param data: Data a etre inserer dans la liste
        """
        node = Node(data, None)
        tail: Node = self.chercher_dernier()
        if tail is not None:
            tail.next = node
        else:
            self.head = node

    def position(self, index):
        """
        Cherche un element dans l'index
        :param index: Position de l'item chercher
        :return: l'item rechercher a l'index precise
        """
        livre: int = 0
        node: Node = self.head
        while node is not None and livre < index:
            livre += 1
            node = node.next
        return node.data

    def chercher_dernier(self) -> Node:
        """
        Trouve le dernier item de la liste.
        :return: le dernier item de la liste, si vide, retourne None
        """
        node: Node = self.head
        while node is not None and node.next is not None:
            node = node.next
        return node

    def __str__(self):
        """
        :return: Retourne un forma string de l'objet library
        """
        node: Node = self.head
        string: str = ""
        while node is not None:
            string += str(node)
            node = node.next
        return string
