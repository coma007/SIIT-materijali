import operator

if __name__ == '__main__':

    d = {"one": 1, "two": 2, "three": 3}
    print(d)
    # sort by key
    sorted_list_by_key = sorted(d.items(), key=operator.itemgetter(0))
    print(sorted_list_by_key)

    # sort by value
    sorted_list_by_value = sorted(d.items(), key=operator.itemgetter(1))
    print(sorted_list_by_value)

    # alternative:
    sorted_list_by_key = sorted(d.items(), key=lambda item: item[0])
    sorted_list_by_value = sorted(d.items(), key=lambda item: item[1])

