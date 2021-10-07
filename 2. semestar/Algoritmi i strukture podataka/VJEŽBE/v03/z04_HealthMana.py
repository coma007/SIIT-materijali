# v03z04
# Implementacija igrice Health Mana

import abc


class Player(object):

    def __init__(self, health, mana):
        self._health = health
        self._mana = mana

    def __str__(self):
        return "health: " + str(self._health) + " mana: " + str(self._mana) + "\n"

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = value


class Item(abc.ABC):

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return "value: " + str(self._value)

    @abc.abstractmethod
    def use(self, player):
        pass


class Food(Item):

    def __init__(self, value):
        super().__init__(value)

    def use(self, player):
        player.health += self._value


class Potion(Food):

    def __init__(self, value, type):
        super().__init__(value)
        self._type = type

    def __str__(self):
        return "value: " + str(self._value) + " type: " + str(self._type)

    def use(self, player):
        if self._type.lower() == "mana":
            player.mana += self._value
        if self._type.lower() == "health":
            player.health += self._value


if __name__ == '__main__':

    player1 = Player(100, 100)
    print(player1)

    food1 = Food(100)
    potion1 = Potion(200, "health")
    potion2 = Potion(300, "mana")

    items = [food1, potion1, potion2]
    for item in items:
        print(item)
        item.use(player1)
        print(player1)
