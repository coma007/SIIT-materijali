class TreeNode(object):
    """
    Klasa modeluje čvor stabla.
    """
    __slots__ = 'parent', 'children', 'data'

    def __init__(self, data):
        """
        Konstruktor.

        Argument:
        - `data`: podatak koji se upisuje u čvor
        """
        self.parent = None
        self.children = []
        self.data = data

    def is_root(self):
        """
        Metoda proverava da li je čvor koren stabla.
        """
        return self.parent is None

    def is_leaf(self):
        """
        Metoda proverava da li je čvor list stabla.
        """
        return len(self.children) == 0

    def add_child(self, x):
        """
        Metoda dodaje potomka čvoru.

        Argument:
        - `x`: čvor potomak
        """
        # kreiranje dvosmerne veze između čvorova
        x.parent = self
        self.children.append(x)

    def __str__(self):
        return str(self.data)

if __name__ == '__main__':

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    print(b)