# autor: Imenko Prezimić INDEX ra1234-2017

izraz_maks_d = 101
rezultat_str: .fill izraz_maks_d    # ovde smestiti stringovnu reprezentaciju rezultata i ne menjati naziv promenljive

# NE MENJATI TEKST PORUKA!
poruka_ulaz: .ascii "Unesite izraz: \0"
poruka_rez: .ascii "Rezultat je: \0"
poruka_greska1: .ascii "Unet je prazan izraz!\n\0"
poruka_greska2: .ascii "U nekoj od ulaznih vrednosti postoji cifra koja ne pripada brojnoj osnovi!\n\0"
poruka_greska3: .ascii "Doslo je do prekoracenja prilikom konverzije nekog od operanada!\n\0"
poruka_greska4: .ascii "Doslo je do prekoracenja prilikom sabiranja!\n\0"

