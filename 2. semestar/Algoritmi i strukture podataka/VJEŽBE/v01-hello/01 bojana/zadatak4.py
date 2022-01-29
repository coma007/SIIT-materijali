"""
Program određuje broj koji generiše najdužu Collatz sekvencu.
"""
import time

MAX_VALUE = 1000000

def generate_next(n):
    """
    Funkcija generiše sledeći element u sekvenci na osnovu tekućeg.

    Argument:
    - `n`: tekući element
    """
    if n % 2 == 0:
        return n//2
    else:
        return 3*n + 1


def collatz_sequence_brute_force():
    """
    Pretraga dužina razvoja kreće od 1 naviše.
    """
    # čuva dužine sekvenci, indeksi su polazni brojevi
    seq_lengths = [0, 1]

    for i in range(2, MAX_VALUE):
        n = i
        seq_length = 0
        done = False

        while n > 1:
            n = generate_next(n)
            seq_length += 1

        seq_lengths.append(seq_length)

    seq_length = max(seq_lengths)
    number = seq_lengths.index(seq_length)
    return number, seq_length

def collatz_sequence_list_only_lower():
    """
    Pretraga dužina razvoja kreće od 1 naviše. Prilikom razvoja svakog broja, uzima se u obzir da je dužina razvoja svih
    brojeva manjih od njega poznata pa se taj podatak koristi za ubrzanje.
    """
    # čuva dužine sekvenci, indeksi su polazni brojevi
    seq_lengths = [0, 1]

    for i in range(2, MAX_VALUE):
        n = i
        seq_length = 0
        done = False

        while n > 1 and not done:
            n = generate_next(n)

            # dužina sekvence za broj n je već izračunata
            if n < len(seq_lengths):
                seq_length += seq_lengths[n]
                done = True

            seq_length += 1

        seq_lengths.append(seq_length)

    seq_length = max(seq_lengths)
    number = seq_lengths.index(seq_length)
    return number, seq_length


def get_sequence_length(number, list):
    """
    Pomoćna funkcija u primeru collatz_sequence_list_caching_all
    :param number: broj čija dužina razvoja se izračunava
    :param list: lista u kojoj su zabeležene do sada izračunate dužine razvoja
    :return: dužina razvoja
    """
    if number == 1:
        return 1

    if number < len(list) and list[number] != 0:
        return list[number]

    next = generate_next(number)

    value = 1 + get_sequence_length(next, list)

    if number<len(list):
        list[number] = value
    return value


def collatz_sequence_list_caching_all():
    """
    Rešenje čuva podatke dužinama razvoja izračunatih u bilo kom trenutku. Svaki broj se razvija tačno jednom.
    Razvoji koji izlaze iz opsega [1,1 000 000] se samo računaju, ali ne i skladište.
    """
    seq_lengths = [0, 1] + 1000000*[0]

    for i in range(2, MAX_VALUE):
        get_sequence_length(i, seq_lengths)

    seq_length = max(seq_lengths)
    number = seq_lengths.index(seq_length)
    return number, seq_length


if __name__ == '__main__':


    print('=== Brute force ===')
    start_time = time.time()
    number, seq_length = collatz_sequence_brute_force()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Number: %d, sequence length: %d' % (number, seq_length))
    print('Elapsed time: %fs' % elapsed_time)

    print('\n\n=== Caching only lower===')
    start_time = time.time()
    number, seq_length = collatz_sequence_list_only_lower()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Number: %d, sequence length: %d' % (number, seq_length))
    print('Elapsed time: %fs' % elapsed_time)

    print('\n\n=== Caching all values ===')
    start_time = time.time()
    number, seq_length = collatz_sequence_list_caching_all()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('\nNumber: %d, sequence length: %d' % (number, seq_length))
    print('Elapsed time: %fs' % elapsed_time)