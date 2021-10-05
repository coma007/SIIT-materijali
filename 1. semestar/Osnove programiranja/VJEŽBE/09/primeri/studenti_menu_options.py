studenti = {}
putanja = "studenti.txt"

def is_int(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False

def novi_student(sifra, ime, prezime):
    student = {"sifra":sifra, "ime": ime, "prezime":prezime}
    studenti[sifra] = student

def unos():
    while True:
        sifra = input("Unesite šifru:")
        if not is_int(sifra):
            print("Unos mora biti ceo broj.")
            continue

        sifra = int(sifra)
        if sifra not in studenti:
            break

        print("Šifra već postoji.")

    ime = input("Unesite ime:")
    prezime = input("Unesite prezime:")
    novi_student(sifra, ime, prezime)

def izmena():
    while True:
        sifra = input("Unesite šifru:")
        if not is_int(sifra):
            print("Unos mora biti ceo broj.")
            continue

        sifra = int(sifra)
        if sifra in studenti:
            break

        print("Šifra ne postoji.")

    novo_ime = input("Unesite novo ime:")
    novo_prezime = input("Unesite novo prezime:")

    student = studenti[sifra]
    student["ime"] = novo_ime
    student["prezime"] = novo_prezime

def ispis():
    print("\nIspis studenata")
    for student in studenti.values():
        print("%-5s %-15s %-15s" % (student["sifra"], student["ime"], student["prezime"]))

def ucitaj():
    with open(putanja) as fajl:
        linije = fajl.readlines()
        for linija in linije:
            linija = linija.replace("\n", "")
            podaci = linija.split("|")
            novi_student(int(podaci[0]), podaci[1], podaci[2])

def sacuvaj():
    with open(putanja, "w") as fajl:
        for student in studenti.values():
            student_str = "{}|{}|{}\n".format(student["sifra"], student["ime"], student["prezime"])
            fajl.write(student_str)

def izlaz():
    print("Odabrali ste izlazak iz aplikacije.")

def izmeni_putanju():
    global putanja
    putanja = input("Unesite putanju:")


def menu():

    menu_dict = {
        '1': unos,
        '2': izmena,
        '3': ispis,
        '4': sacuvaj,
        '5': ucitaj,
        '6': izmeni_putanju,
        'x': izlaz
    }

    while True:
        print("=" * 30)
        print("Glavni meni aplikacije")
        print("=" * 30)
        print("Ponuđene opcije:")
        print("1. Unos studenta\n2. Izmena studenta\n3. Ispis svih studenata\n4. Čuvanje\n"
              "5. Učitavanje podataka iz fajla\n6. Izmena putanje fajla\nx. Izlaz")

        user_input = input(">>")

        if user_input in menu_dict:
            menu_dict[user_input]()
            if user_input == 'x':
                return
        else:
            print("Odabrali ste nepostojeću opciju")


if __name__ == '__main__':
    menu()