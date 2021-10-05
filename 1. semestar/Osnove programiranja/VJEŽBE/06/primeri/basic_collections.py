def main():
    collection = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(collection[1:])
    print(collection[3:7:2])

    variable = 4 > 11

    if variable:
        print("variable je True")

    new_coll = []
    for elem in collection:
        new_coll.append(elem)

    new_coll = [0] * len(collection)
    for i in range(len(collection)):
        i += 2
        new_coll[i] = collection[i]

    for i, elem in enumerate(collection):
        print("Na indeksu", i, "se nalazi element",elem)

    skip_collection = [False, True, False, False, True]
    for item in skip_collection:
        if item:
            break
        print(item)



if __name__ == '__main__':
    main()
