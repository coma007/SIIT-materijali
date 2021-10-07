# v02z04
# Napisati rekurzivnu funkciju za replikaciju. Funkcija ima dva parametra – prvi je	broj koji treba umnožiti,
# a	drugi broj ponavljanja.


def replicate_list(number, times):

    if times == 0:
        return []
    if times == 1:
        return [number]
    return [number] + replicate_list(number, times-1)


if __name__ == '__main__':

    print("------Creating uniform list with replication------")
    print(f"List of {6} {5}s: {replicate_list(5, 6)}")
