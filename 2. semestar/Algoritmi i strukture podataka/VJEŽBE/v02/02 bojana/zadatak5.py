"""
Program demonstrira upotrebu rekurzije u pretraživanju direktorijumskog stabla.
"""
import os


def find(path):
    """
    Funkcija pretražuje direktorijumsko stablo počevši od zadate putanje i
    ispisuje apsolutne putanje svih pronađenih fajlova.

    Argument:
    - `path`: polazna putanja
    """
    #štampa se apsolutna putanja bilo da se na trenutnoj putanji path nalazi fajl ili folder
    print(os.path.abspath(path))
    # bazni slučaj: putanja je običan fajl
    if not os.path.isdir(path):
        return
    files = os.listdir(path)
    for filename in files:
        find(os.path.join(path, filename))


if __name__ == '__main__':
    path = input('Unesi polaznu putanju: ')
    if os.path.lexists(path):
        find(path)
    else:
        print("Uneta putanja ne postoji")
