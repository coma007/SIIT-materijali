def item_counter(collection, item):
    counter = 0
    for i in collection:
        if i == item:
            counter += 1
    return counter


def main():
    collection = [1, 6, 5, 9, 2, 5, 8, 9, 5, 7]
    counter = item_counter(collection, 5)

    if counter == 0:
        print("U kolekciji nema elementa koji tražite.")
    else:
        print("Element koji tražite se pojavljuje", counter, "puta.")


if __name__ == '__main__':
    main()
