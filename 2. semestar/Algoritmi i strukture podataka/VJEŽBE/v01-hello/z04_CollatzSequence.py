# v01z04 - Naći	pozitivan broj n na	osnovu koga	se kreira najduži niz elemenata prema sledećem pravilu:
# n_i+1 = n_i / 2 ako je n_i paran
# n_i+1 = 3 * n_i + 1 ako je n_i neparan

from time import time


# brute force solution
def generate_array(n):

    lista = [n]
    if n in tmp.keys():
        lista += tmp[n][0]
    else:
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                lista.append(n)
            else:
                n = 3 * n + 1
                lista.append(n)
    return lista, len(lista)


tmp = {}


def brute_force(border):

    max_len = 0
    max_i = 0
    for i in range(1, border+1):
        tmp[i] = generate_array(i)
        if tmp[i][1] > max_len:
            max_len = tmp[i][1]
            max_i = i

    return max_i, max_len

###########################################


# thoughtful solution
def generate_element(n):

    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def save_all_lengths_solution(border):

    lengths = [0, 1]
    for i in range(2, border):
        length = 0
        while i != 1:
            i = generate_element(i)
            length += 1
            if i < len(lengths):
                lengths.append(lengths[i]+length)
                break
    return max(lengths), lengths.index(max(lengths))

###########################################


# the best solution
def get_length(number, lengths):

    if number == 1:
        return 1

    if number < len(lengths) and lengths[number] != 0:
        return lengths[number]

    next_number = generate_element(number)
    this_length = 1 + get_length(next_number, lengths)

    if number < len(lengths):
        lengths[number] = this_length
    return this_length


def save_some_lengths_solution(border):

    lengths = [0, 1] + [0] * border
    for i in range(2, border):
        get_length(i, lengths)

    return max(lengths), lengths.index(max(lengths))


if __name__ == '__main__':

    print("------The Biggest Collatz Array------")

    start = time()
    print("\n#Brute force")
    data = brute_force(10**6)
    print("Base number: ", data[0], "\nNumber of elements: ", data[1])
    print("Elapsed time: ", time()-start)

    start = time()
    print("\n#Solution with list of all lengths")
    data = save_all_lengths_solution(10 ** 6)
    print("Base number: ", data[1], "\nNumber of elements: ", data[0])
    print("Elapsed time: ", time()-start)

    start = time()
    print("\n#Solution with list of some lengths")
    data = save_some_lengths_solution(10**6)
    print("Base number: ", data[1], "\nNumber of elements: ", data[0])
    print("Elapsed time: ", time()-start)
