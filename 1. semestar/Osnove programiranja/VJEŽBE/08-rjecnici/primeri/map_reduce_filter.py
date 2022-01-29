def filter_examples():
    # oblika filter(function, sequence)
    # vraća novu sekvencu sačinjenu od elemenata koji zadovoljavaju
    # uslov iz funkcije (za koju zadata funkcija vraća True)

    # samo parni elementi stare liste u novoj
    stara_lista = [1, 2, 3, 4, 5, 6]
    nova_lista = filter(lambda x: x % 2 == 0, stara_lista)
    for item in nova_lista:
        print(item, end=" ")

    print()
    # Izdvajamo podatke vezane za korisnike sa zadatim imenom
    podaci = ["1|Pera", "2|Sima", "3|Jovica", "4|Pera"]
    trazeni_korisnik = "Pera"

    unosi_trazenog_korisnika = filter(lambda x: trazeni_korisnik in x, podaci)
    for item in unosi_trazenog_korisnika:
        print(item, end=" ")

    print()

def map_examples():
    # oblika map(function, sequence)
    # Nad svakim elementom sekvence sequence se poziva zadata funkcija
    # rezultat te funkcije se vraća kao rešenje

    # u novu listu ubacujemo kvadrate elemenata stare liste
    stara_lista = [1, 2, 3, 4, 5, 6]
    nova_lista = map(lambda x: x**2, stara_lista)

    for item in nova_lista:
        print(item, end=" ")

    print()

    # Konvertujemo listu stringova u splitovan oblik
    podaci = ["1|Pera", "2|Sima", "3|Jovica", "4|Pera"]

    splitovani_podaci = map(lambda x: x.split("|"), podaci)

    for item in splitovani_podaci:
        print(item, end=" ")

    print()

# Funkcija reduce je bila deo osnovne biblioteke u Pythonu 2. U Python-u 3 je izbačena.
# Razlozi (citat Guida van Rossuma):
# "So now reduce(). This is actually the one I've always hated most, because, apart from a few examples involving + or *,
# almost every time I see a reduce() call with a non-trivial function argument, I need to grab pen and paper to diagram
# what's actually being fed into that function before I understand what the reduce() is supposed to do. So in my mind,
# the applicability of reduce() is pretty much limited to associative operators, and in all other cases it's better to
# write out the accumulation loop explicitly."

# Ipak, može da se importuje iz modula functools
from functools import reduce
def reduce_examples():
    # oblika reduce(function, sequence)
    #  cela sekvenca sequence se redukuje (svodi) na jednu vrednosti
    #  na osnovu funkcije function

    # sumiramo elemente stare liste
    stara_lista = [1, 2, 3, 4, 5, 6]
    rezultat = reduce(lambda x, y: x+y, stara_lista)
    print(rezultat)


# kako reduce radi
def my_reduce(function, sequence):
    result = sequence[0]
    for next in sequence[1:]:
        result = function(result, next)

    return result


if __name__ == '__main__':
    while True:
        print("Odaberite jednu od opcija:")
        print("1. Filter examples\n2. Map examples \n3. Reduce examples\nx. Izlazak\n")
        options = {
            '1': filter_examples,
            '2': map_examples,
            '3': reduce_examples,
            'x': exit
        }
        user_input = input(">>")
        options[user_input]()
