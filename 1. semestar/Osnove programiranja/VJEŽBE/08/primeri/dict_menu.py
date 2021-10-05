def opcija1():
    print("Odabrali ste opciju 1.")


def opcija2():
    print("Odabrali ste opciju 2.")


def opcija3():
    print("Odabrali ste opciju 3.")


def izlaz():
    print("Odabrali ste opciju za izlazak iz programa.")
    exit()

def ispis_menija():
    print("Odaberite jednu od dostupnih opcija:")
    print("1. Opcija 1")
    print("2. Opcija 2")
    print("3. Opcija 3")
    print("x. Izlazak iz programa.")


if __name__ == '__main__':

    meni = {
        '1': opcija1,
        '2': opcija2,
        '3': opcija3,
        'x': izlaz
    }

    while True:
        ispis_menija()
        unos = input(">>")
        if unos in meni.keys():
            odabrana_funkcija = meni[unos]
            odabrana_funkcija()
        else:
            print("Odabrali ste nepostojeću opciju.")

