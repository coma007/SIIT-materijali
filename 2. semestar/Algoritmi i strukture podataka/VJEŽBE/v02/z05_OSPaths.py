# v02z05
# Prikazati	apsolutne putanje svih datoteka na zadatoj putanji u direktorijumskom stablu.

import os


def find(path):

    print(os.path.abspath(path))
    if not os.path.isdir(path):
        return None
    files = os.listdir(path)
    for file in files:
        find(os.path.join(path, file))


if __name__ == '__main__':

    print("------Absolut Paths in Directorium------")

    my_path = input("\nInput path of existing directorium: ")
    if os.path.lexists(my_path):
        find(my_path)
    else:
        print("The path does not exist !")
