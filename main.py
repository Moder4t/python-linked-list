from labo01.library import Library, LinkedList
from labo01.livre import JOURS_MAX


def chercher_clients(ajd: int) -> int:
    accepter = False
    clients = 0
    while not accepter:
        try:
            clients: int = int(
                input(f"Nous sommes le jour {ajd}, combien de client(s)?")
            )
            if clients < 1:
                print("Le nombre doit être positif")
            else:
                accepter = True
        except ValueError:
            print("Veuillez saisir un nombre entier")
    return clients


def chercher_livre_clients(client: int) -> int:
    accepter = False
    livre = 0
    while not accepter:
        try:
            livre: int = int(input(f"Client {client}: indice du livre réservé?"))
            if livre < 1:
                print("L'indice doit être compris entre 0 et 9")
            else:
                accepter = True
        except ValueError:
            print("Veuillez saisir un indice de livre")
    return livre


# programme main
def main():

    library = Library()
    ajd = 1

    # boucle infinie
    while True:

        # cree une liste des livres
        livres: LinkedList = LinkedList()
        clients: int = chercher_clients(ajd)
        for client in range(clients):
            livre: int = chercher_livre_clients(client)
            livres.ajout_dernier(livre)

        # perform book reservations
        for client in range(clients):
            try:
                livre: int = livres.position(client)
                library.reservation_de_livre(client, livre, ajd)
                print(
                    f"Cher client {client}, le livre {livre} vous est bien réservé pour {JOURS_MAX} jours"
                )
            except Exception as e:
                print(e)

        ajd += 1

        library.retour_de_livre(ajd)


# program entry point
if __name__ == "__main__":
    main()
