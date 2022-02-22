from library import Library
from livre import Livre
import pytest


class TestReservation:

    CLIENT0 = 0
    CLIENT1 = 1
    LIVRE0 = 0
    AJD = 1

    def test_reservation_de_livre(self):
        library: Library = Library()

        library.reservation_de_livre(self.CLIENT0, self.LIVRE0, self.AJD)
        livre: Livre = library.verification_livre(self.LIVRE0)

        assert livre.deja_reserver is True

    def test_livre_deja_reserver(self):
        library: Library = Library()

        library.reservation_de_livre(self.CLIENT0, self.LIVRE0, self.AJD)

        with pytest.raises(Exception):
            library.reservation_de_livre(self.CLIENT1, self.LIVRE0, self.AJD)
