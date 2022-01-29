#Brojanje pojavljivanja za svaki elemenata zadate liste
if __name__ == '__main__':

    lista = ["slavko2", "milan34", "jovan1", "slavko2", "slavko2", "milan34"]

    lista_bez_duplikata = []
    ponavljanja = []

    for user in lista:
        for i in range(len(lista_bez_duplikata)):
            if lista_bez_duplikata[i] == user:
                ponavljanja[i] += 1
                break
        else:
            lista_bez_duplikata.append(user)
            ponavljanja.append(1)

    for user, count in zip(lista_bez_duplikata, ponavljanja):
        print("Korisnik", user, "se pojavljuje", count, "puta.")

    # for i, user in enumerate(lista_bez_duplikata):
    #     print(i, user)

    dict = {}

    for user in lista:
        if user in dict:
            dict[user] += 1
        else:
            dict[user] = 1








