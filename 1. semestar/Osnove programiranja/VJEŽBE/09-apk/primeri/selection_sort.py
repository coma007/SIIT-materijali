# funkcija pretty_print nam pomaže da lakše vizualizujemo proces sortiranja
def pretty_print(collection, first, second):

    for index, element in enumerate(collection):
        if index==first or index==second:
            content = "[{}]".format(element)
        else:
            content = "{}".format(element)

        print("{:^4}".format(content), end="")

    print()

def sort(collection):
    n = len(collection)

    # indeks i odgovara fiksiranoj poziciji za koju pronalazimo odgovarajući element
    # npr. na poziciji 0 treba da se nađe najmanji element
    for i in range(n-1):
        # indeks j odgovara elementima sa kojim poredimo element na poziciji i
        for j in range(i+1, n):
            # štampamo elemente koje poredimo
            pretty_print(collection, i, j)
            # pošto je indeks i uvek manji od j, element na poziciji i bi trebalo da bude manji od
            # elementa na poziciji j u sortiranoj kolekciji
            # Ukoliko nije trenutno, zamenjujemo elemente na poziciji i i j
            if collection[i]>collection[j]:
                collection[i], collection[j] = collection[j], collection[i]
            # štampamo stanje kolekcije posle poređenja
            pretty_print(collection, i, j)
        print("\n")

if __name__ == '__main__':
    a = [6, 8, 3, 9, 1, 7, 5, 2]
    print("Collection:", a)
    sort(a)
    print("Sorted collection:", a)
