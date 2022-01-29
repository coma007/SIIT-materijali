sifre = [2, 6, 7]
imena = ["Pera", "Mika", "Steva"]


def print_by_index():
    print("\n{:^10}{:^10}".format("Šifra", "Ime"))
    print("="*20)
    for i in range(len(sifre)):
        print("{:^10}{:^10}".format(sifre[i], imena[i]))


def print_enumerate():
    print("\n{:^10}{:^10}".format("Šifra", "Ime"))
    print("="*20)
    for i, sifra in enumerate(sifre):
        print("{:^10}{:^10}".format(sifra, imena[i]))


def print_zip():
    print("\n{:^10}{:^10}".format("Šifra", "Ime"))
    print("="*20)
    for sifra, ime in zip(sifre, imena):
        print("{:^10}{:^10}".format(sifra, ime))


if __name__ == '__main__':
    print_by_index()
    print_enumerate()
    print_zip()



