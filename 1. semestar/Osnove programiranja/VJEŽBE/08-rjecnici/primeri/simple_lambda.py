def inc(x):
    return x+1

if __name__ == '__main__':

    #definišemo anonimnu funkciju
    inc = lambda x: x+1
    print(inc(3))

    # ili kraće
    # print (lambda x:x+1)(3)

    proveri_parnost = lambda x: x % 2 == 0

    print(proveri_parnost(5))
    print(proveri_parnost(6))

    sabiranje = lambda x, y: x+y
    print(sabiranje(1,2))