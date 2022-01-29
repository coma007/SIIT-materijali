users = {}

def insert(id, first_name, last_name):
    # Proveravamo jedninstvenost identifikatora
    if id not in users:
        # Kreiramo novi rečnik za novog korisnika
        # Novi rečnik vezujemo na ključ koji odgovara identifikatoru
        users[id] = {"id":id, "first_name": first_name, "last_name": last_name}
    else:
        print("Korisnik sa traženim identifikatorom već postoji. Dodavanje nije uspelo.")

def print_data():
    print("{:^4} {:^15} {:^15}".format("ID", "First name", "Last name"))
    print("="*40)
    for user in users.values():
        current_id = user["id"]
        current_first_name = user["first_name"]
        current_last_name = user["last_name"]
        print("{:^4} {:^15} {:^15}".format(current_id, current_first_name, current_last_name))
    print("\n")

def change(id, new_first_name, new_last_name):
    if id in users:
        # Pronašli smo korisnika koji ima isti identifikator onom koji unosimo
        # Prelazimo na izmenu podataka
        users[id]["first_name"] = new_first_name
        users[id]["last_name"] = new_last_name
    else:
        print("Traženi korisnik ne postoji. Izmena nije uspela.")

if __name__ == '__main__':
    insert(11, "Ivana", "Nikolić")
    insert(2, "Milan", "Milić")
    print_data()
    change(11, "Ivana", "Jovanović")
    print_data()