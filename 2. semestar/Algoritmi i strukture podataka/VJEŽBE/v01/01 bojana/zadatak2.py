"""
Program izračunava najveći palindrom nastao kao proizvod trocifrenih brojeva.
Moguće je i kombinovanje pristupa u cilju povećavanja efikasnosti.
"""
import time, math

def max_palindrome_brute_force():
    """
    Rešenje grubom silom
    """
    max_palindrome = 0
    # generisanje svih proizvoda trocifrenih brojeva
    for i in range(100, 1000):
        for j in range(100, 1000, 1):
            current = i*j

            if int(str(current)[::-1]) == current and current > max_palindrome:
                max_palindrome = current

    return max_palindrome


def max_palindrome_simetric():
    """
    Rešenje bazirano na uočenoj simetriji matrice proizvoda.
    """
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(999, i-1, -1):
            current = i*j

            if int(str(current)[::-1]) == current and current > max_palindrome:
                max_palindrome = current

    return max_palindrome



def _max_palindrome_11_division():
    """
    Rešenje bazirano na zaključku da je traženi proizvod-palindrom deljiv sa 11.
    Broj je deljiv sa 11 ako je razlika između zbira cifara na neparnim pozicijama i parnim pozicijama deljiva sa 11.
    Dovoljno je za prvi broj uzeti broj deljiv sa 11. U ovom rešenju ne možemo da uzmemo u obzir simetričnost matrice, zbog
    potencijalnog preskakanja rešenja.
    """
    max_palindrome = 0
    for i in range(110, 1000, 11):
        for j in range(100, 1000):
            current = i*j

            if int(str(current)[::-1]) == current and current > max_palindrome:
                max_palindrome = current

    return max_palindrome


def max_palindrome_optimized_lanes():
    """
    Pronalaženje najvećeg palindroma pretragom po 'trakama'. Rešenje se bazira na posmatranju proizvoda jednog fiksiranog
    broja iz prve petlje (recimo 999) i brojeva s kojim se on množi iz druge petlje. S obzirom da brojevi u drugoj petlji
    opadaju, možemo zaključiti da i proizvodi prvog fiksnog broja i drugog opadaju. Na osnovu toga zaključujemo da možemo da
    prekinemo pretragu po traci čim pronađemo prvi palindrom (jer nema šanse da nađemo većeg u okviru iste trake). Posle toga
    se prelazi na sledeću traku. Posmatramo proizvode i iz druge trake. Proizvodi se postepeno smanjuju. Ako uočimo da opadaju
    ispod granice našeg maksimuma, zaključujemo da nije moguće pronaći veći proizvod (pa samim tim ni proizvod palindrom)
    u toj traci, pa se prelazi na sledeću. Takođe, ako u nekoj od sledećih traka pronađemo palindrom veći od našeg dotadašnjeg
    maksimuma, prelazimo na sledeću traku.
    """
    max_palindrome = 0
    for i in range(999, 100, -1):
        for j in range(999, i-1, -1):
            current = i*j
            if current <= max_palindrome:
                break
            if int(str(current)[::-1]) == current:
                max_palindrome = current
                break
    return max_palindrome


def max_palindrome_product_search():
    """
    Ideja ovog pristupa je da se pretražuju šestocifreni i petocifreni brojevi (u opsegu od 999*999 do 100*100). Kada se
    utvrdi da je broj-kandidat palindrom, pokušavamo da utvrdimo da li je broj proizvod dva trocifrena broja. Prvi broj
    koji pronađemo da odgovara uslovima pretrage (palindrom je i proizvod dva trocifrena broja) je ujedno i rešenje.
    """
    max_potential_value = 999*999
    min_potential_value = 100*100
    for current in range(max_potential_value, min_potential_value, -1):
        if int(str(current)[::-1]) == current:
            root_value = int(math.floor(math.sqrt(current)))
            for divisor in range(root_value, 99, -1):
                n = current // divisor
                if n >= 1000:
                    break
                if current % divisor == 0:
                        return current


def max_palindrome_greatest_palindrome_search():
    """
    Formiraju se svi šestocifreni palindromi od najvećeg do najmanjeg. Za svaki od njih, pokušavamo da utvrdimo da li je
    proizvod dva trocifrena broja (odnosno da li je deljiv sa nekim trocifrenim brojem, pri čemu bi i rezultat deljenja
    trebalo da bude trocifren broj)
    """
    max_potential_value = 1000
    min_potential_value = 99
    current_value = max_potential_value
    max_number_of_palindrome_digits = 6
    min_number_of_palindrome_digits = 5
    current_number_of_palindrome_digits = max_number_of_palindrome_digits

    while current_number_of_palindrome_digits >= min_number_of_palindrome_digits: # uzimamo u obzir i šestocifrene i
        # petocifrene palindrome. Prvo pretražujemo šestocifrene, pa ako među njima nema nijednog koji je proizvod
        # dva trocifrena broja, prelazimo na petocifrene
        while current_value > min_potential_value:
            current_value -= 1
            str_current_value = str(current_value)
            str_current_palindrome = str_current_value + str_current_value[::-1]
            current_palindrome = int(str_current_palindrome)

            root_palindrome_value = int(math.floor(math.sqrt(current_palindrome)))
            for divisor in range(root_palindrome_value, 99, -1):
                n = current_palindrome // divisor
                # uspešno smo podelili palindrom, ali je drugi činilac četvorocifren
                if n >= 1000:
                    break
                if current_palindrome % divisor == 0:
                    return current_palindrome
        current_number_of_palindrome_digits -= 1


if __name__ == '__main__':

    start_time = time.time()
    max_palindrome_brute_force = max_palindrome_brute_force()
    elapsed_time = time.time() - start_time
    print('Brute force solution: %d' % max_palindrome_brute_force)
    print('Elapsed time: ' + str(elapsed_time))

    start_time = time.time()
    max_palindrome_simetric = max_palindrome_simetric()
    elapsed_time = time.time() - start_time
    print('\nSimetric solution: %d' % max_palindrome_simetric)
    print('Elapsed time: ' + str(elapsed_time))

    start_time = time.time()
    _max_palindrome_11_division = _max_palindrome_11_division()
    elapsed_time = time.time() - start_time
    print('\nDivision by 11 solution: %d' % _max_palindrome_11_division)
    print('Elapsed time: ' + str(elapsed_time))

    start_time = time.time()
    max_palindrome_optimized_lanes = max_palindrome_optimized_lanes()
    elapsed_time = time.time() - start_time
    print('\nOptimized lanes solution: %d' % max_palindrome_optimized_lanes)
    print('Elapsed time: ' + str(elapsed_time))

    start_time = time.time()
    max_palindrome_product_search = max_palindrome_product_search()
    elapsed_time = time.time() - start_time
    print('\nMax palindrome product search solution: %d' % max_palindrome_product_search)
    print('Elapsed time: ' + str(elapsed_time))

    start_time = time.time()
    max_palindrome_greatest_palindrome_search = max_palindrome_greatest_palindrome_search()
    elapsed_time = time.time() - start_time
    print('\nMax palindrome greatest palindrome search solution: %d' % max_palindrome_greatest_palindrome_search)
    print('Elapsed time: ' + str(elapsed_time))

