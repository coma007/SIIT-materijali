users = []

def insert(id, first_name, last_name):
    # Proveravamo jedninstvenost identifikatora
    found = False
    for current_user in users:
        if current_user[0] == id:
            # Pronašli smo korisnika koji ima isti identifikator onom koji unosimo
            # dodavanje ne bi trebalo dozvoliti
            found = True
            break

    if not found:
        # dodajemo samo ako nismo pronašli korisnika sa istim identifikatorom
        users.append([id, first_name, last_name])
    else:
        print("Korisnik sa traženim identifikatorom već postoji. Dodavanje nije uspelo.")

def print_data():
    print("{:^4} {:^15} {:^15}".format("ID", "First name", "Last name"))
    print("="*40)
    for i in range(len(users)):
        current_id = users[i][0]
        current_first_name = users[i][1]
        current_last_name = users[i][2]
        print("{:^4} {:^15} {:^15}".format(current_id, current_first_name, current_last_name))
    print("\n")

def change(id, new_first_name, new_last_name):
    # Da bi smo izvršili izmenu, pronalazimo indeks (poziciju) traženog korisnika
    found = False
    for i in range(len(users)):
        if users[i][0] == id:
            # Pronašli smo korisnika koji ima isti identifikator onom koji unosimo
            # Prelazimo na izmenu podataka
            users[i][1] = new_first_name
            users[i][2] = new_last_name
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