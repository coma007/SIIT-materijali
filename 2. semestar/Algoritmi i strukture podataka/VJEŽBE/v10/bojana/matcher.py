"""
Modul sadrži implementacije algoritama za pretraživanje teksta
"""


def brute_force(T, P):
    """
    Brute force algoritam pretrage

    Funkcija poredi odgovarajuće karaktera teksta i šablona koji
    se traži. Svako nepoklapanje pomera startnu poziciju pretrage
    za 1. Složenost: O(nm), gde su n i m dužine teksta odnosno
    šablona koji se traži.

    Argumenti:
    - `T`: tekst koji se pretražuje
    - `P`: šablon koji se traži
    """
    n = len(T)
    m = len(P)

    found = []
    diff = n-m+1
    for s in range(diff):
        if P == T[s:s+m]:
            found.append(s)

    return found


def boyer_moore(T, P):
    """
    Boyer-Moore algoritam pretrage

    Funkcija poredi odgovarajuće karaktera teksta i šablona koji
    se traži sa desna nalevo. Svako nepoklapanje pomera startnu
    poziciju pretrage za broj koraka koji se računa na osnovu
    poslednjeg pojavljivanja nepoklopljenog karaktera iz teksta u šablonu.
    Složenost: O(nm+s), gde su n i m dužine teksta odnosno šablona koji se
    traži, a s predstavlja dužinu alfabeta.

    Argumenti:
    - `T`: tekst koji se pretražuje
    - `P`: šablon koji se traži
    """
    n, m = len(T), len(P)
    #trivijalno traženje za prazan string
    if m == 0:
        return 0
    last = {}
    #popunjavanje rečnika tako da se beleže poslednje pojave karaktera u šablonu
    for k in range(m):
        last[ P[k] ] = k
    # indeksi počinju od kraja šablona
    i = m-1 #indeks teksta
    k = m-1 #indeks šablona
    while i < n:
        #pokušaj poklapanja
        if T[i] == P[k]:
            if k == 0:
                #uspešno poklapanje svih karaktera od kraja šablona do početka, uspešno završeno
                return i
            else:
                #uspešno poklapanje poslednjih k karaktera šablona
                #sledeće poređenje je između prethodnog karaktera teksta i prethodnog karaktera šablona
                i -= 1
                k -= 1
        else:
            #čitanje indeksa nepoklopljenog karaktera teksta iz rečnika
            #j=-1 ukoliko traženi karakter ne postoji u rečniku
            j = last.get(T[i], -1)
            #računanje broja koraka za skok
            i += m - min(k, j + 1)
            #početak analize šablona od kraja (restart)
            k = m - 1

    return -1

def generate_table(P):
    """
    Funkcija generiše tabelu poklapanja za KMP algoritam

    Tabela poklapanja beleži maksimalnu dužinu tzv. `proper`
    prefiksa stringa koji je ujedno i njegov sufiks.

    Argument:
    - `P`: string čija se tabela generiše
    """
    # tabela ima onoliko elemenata koliko string ima karaktera
    m = len(P)
    table = [0] * m

    # broj poklapanja (k) i indeks trenutnog karaktera (i)
    k = 0
    i = 1

    while i < m:
        if P[i] == P[k]:
            # ukoliko se karakteri poklapaju povećava se broj poklopljenih
            table[i] = k+1
            i = i + 1
            k = k + 1
        elif k > 0:
            # karakteri se ne poklapaju, ali je bilo pogodaka, pokušaj pronaći
            # kraći prefiks koji je ujedno i sufiks
            k = table[k-1]
        else:
            # nema poklapanja, pređi na sledeći karakter
            i = i + 1

    return table


def kmp(T, P):
    """
    Knuth-Morris-Pratt algoritam

    Na osnovu generisane tabele, algoritam vrši `pametne` pomeraje
    prilikom pretraživanja stringa. Složenost: O(n+m), gde su n i m
    dužine teksta koji se pretražuje odnosno šablona koji se traži.

    Argumenti:
    - `T`: tekst koji se pretražuje
    - `P`: šablon koji se traži
    """
    n = len(T)
    m = len(P)

    if m == 0:
        return [0]

    # get prefix table
    table = generate_table(P)

    # indeks šablona (k) i indeks trenutnog karaktera (i)
    k = 0
    i = 0

    # lista čuva indekse na kojima počinju poklapanja
    found = []

    while i < n:
        if T[i] == P[k]:
            # ako se karakteri poklapaju proveri da li je došlo do potpunog
            # poklapanja ili povećaj broj poklopljenih karaktera
            if k == m-1:
                found.append(i-m+1)
                k = table[k-1]
            else:
                i = i + 1
                k = k + 1
        elif k > 0:
            # karakteri se ne poklapaju ali je bilo pogodaka, pomeri za
            # odgovarajući broj mesta
            k = table[k-1]
        else:
            # nema poklapanja, pređi na sledeći karakter
            i = i + 1

    return found


if __name__ == '__main__':
    text = 'abaabccbcabbabaab'
    pattern = 'abba'
    print(brute_force(text, pattern))
    print(boyer_moore(text, pattern))
    print(kmp(text, pattern))
