import abc

class Player(object):
    def __init__(self, health, mana):
        self._health = health
        self._mana = mana

    @property
    def health(self):
        return self._health

    @property
    def mana(self):
        return self._mana

    @health.setter
    def health(self, new_value):
        self._health = new_value

    @mana.setter
    def mana(self, new_value):
        self._mana = new_value

    def __str__(self):
        return "Player[health = " + str(self._health) + ", mana = " + str(self._mana) + "]"

class Item(abc.ABC):

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @abc.abstractmethod
    def use(self, player):
        pass

    def __str__(self):
        return "Item[value = " + str(self._value) + "]"

class Food(Item):

    def use(self, player):
        player.health += self._value

    def __str__(self):
        return "Food[value = " + str(self._value) + "]"

class Potion(Item):

    def __init__(self, value, type):
        super().__init__(value)
        self._value = value
        self._type = type

    def use(self, player):
        if self._type.lower() == "health":
            player.health += self._value
        else:
            player.mana += self._value

    def __str__(self):
        return "Potion[value = " + str(self._value) + ", type = " + self._type + "]"

if __name__ == '__main__':
    player = Player(100, 100)
    print(player)

    f1 = Food(100)
    p1 = Potion(200, "health")
    p2 = Potion(300, "mana")

    item_list = [f1, p1, p2]

    for item in item_list:
        print(item)
        item.use(player)
        print(player)

    item = Item(200)
    print(item)


