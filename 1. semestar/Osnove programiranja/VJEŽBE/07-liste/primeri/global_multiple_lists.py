ids = []
first_names = []
last_names = []

def insert(id, first_name, last_name):
    # Proveravamo jedninstvenost identifikatora
    found = False
    for current_id in ids:
        if current_id == id:
            # Pronašli smo korisnika koji ima isti identifikator onom koji unosimo
            # dodavanje ne bi trebalo dozvoliti
            found = True
            break

    if not found:
        # dodajemo samo ako nismo pronašli korisnika sa istim identifikatorom
        ids.append(id)
        first_names.append(first_name)
        last_names.append(last_name)
    else:
        print("Korisnik sa traženim identifikatorom već postoji. Dodavanje nije uspelo.")

def print_data():
    print("{:^4} {:^15} {:^15}".format("ID", "First name", "Last name"))
    print("="*40)
    for i in range(len(ids)):
        current_id = ids[i]
        current_first_name = first_names[i]
        current_last_name = last_names[i]
        print("{:^4} {:^15} {:^15}".format(current_id, current_first_name, current_last_name))
    print("\n")

def change(id, new_first_name, new_last_name):
    # Da bi smo izvršili izmenu, pronalazimo indeks (poziciju) traženog korisnika
    found = False
    for i in range(len(ids)):
        if ids[i] == id:
            # Pronašli smo korisnika koji ima isti identifikator onom koji unosimo
            # Prelazimo na izmenu podataka
            first_names[i] = new_first_name
            last_names[i] = new_last_name
            found = True
            break

    if not found:
        print("Traženi korisnik ne postoji. Izmena nije uspela.")

if __name__ == '__main__':
    insert(11, "Ivana", "Nikolić")
    insert(2, "Milan", "Milić")
    print_data()
    change(11, "Ivana", "Jovanović")
    print_data()