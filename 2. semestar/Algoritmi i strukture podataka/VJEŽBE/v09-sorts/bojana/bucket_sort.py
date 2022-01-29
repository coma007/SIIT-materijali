class Item:
    __slots__ = 'key', 'value'

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + self.key + ', ' + self.value + ')'


def bucket_sort(S):
    length = len(S)
    B = [[]] * length
    for item in S:
        k = item.key
        S.remove(item)
        B[k].append(item)
    for i in range(length):
        for item in B[i]:
            B[i].remove(item)
            S.append(item)
    return S


if __name__ == '__main__':
    item1 = Item(7, 'd')
    item2 = Item(1, 'c')
    item3 = Item(3, 'a')
    item4 = Item(7, 'g')
    item5 = Item(3, 'b')
    item6 = Item(7, 'e')

    S = [item1, item2, item3, item4, item5, item6]

    S = bucket_sort(S)
    for item in S:
        print(item)

