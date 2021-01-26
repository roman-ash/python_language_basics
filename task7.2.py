from abc import ABC, abstractmethod


class Apparel(ABC):

    @abstractmethod
    def count_textile(self):
        pass


class Coat(Apparel):

    def __init__(self, size):
        self._size = size

    @property
    def count_textile(self):
        return round(self._size / 6.5 + 0.5, 2)


class Suit(Apparel):

    def __init__(self, height):
        self._height = height

    @property
    def count_textile(self):
        return round(self._height * 2 + 0.3, 2)


coat = Coat(100)
suit = Suit(20)
print(coat.count_textile)
print(suit.count_textile)
