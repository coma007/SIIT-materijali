if __name__ == '__main__':
    s = [1,2,3,4,5]
    i = 1
    j = 4
    korak = 2

    print(s[i])  # Indeksni pristup
    print(s[i:j])  # Isecanje (slicing)
    print(s[i:j:korak])  # Prošireno isecanje
    print(len(s))  # broj elemenata sekvence
    print(min(s), max(s))  # minimalna/maksimalna vrednosta u sekvenci
    print(sum(s,0))  # sumiranje sekvence
    print(all(s))  # da li su svi elementi sekvence True
    print(any(s))  # da li je bilo koji element u listi True
    for a in s:  # iteracija
        print(a)

    s[i] = 99
    print(s)
    s[i:j] = [100, 101]
    print(s)
    s[i:j:korak] = ['W', 'Q']
    print(s)
    del s[i]
    del s[i:j]
    del s[i:j:korak]