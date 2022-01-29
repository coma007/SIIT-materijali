def insert_in_position(collection, position, element):
    n = len(collection)
    current_position = n-1

    while current_position > position:
        collection[current_position] = collection[current_position-1]
        current_position -= 1

    collection[position] = element

def find_best(collection, best_number):
    result_list = [None]*best_number

    for element in collection:
        for result_index, result in enumerate(result_list):

            if result is None:
                result_list[result_index] = element
                break

            if element[0] < result[0]:
                insert_in_position(result_list, result_index, element)
                break

    return result_list


def find_best_with_sort(collection, best_number):
    n = len(collection)
    for i in range(n-1):
        for j in range(i+1, n):
            if collection[i] > collection[j]:
                collection[i], collection[j] = collection[j], collection[i]

    return collection[:best_number]

if __name__ == '__main__':
    runners = [
                (9.58, 'Usain Bolt'),
                (9.93, 'Patrick Johnson'),
                (9.99, 'Su Bingtian'),
                (9.78, 'Nesta Carter'),
                (9.97, 'Ramil Guliyev'),
                (9.72, 'Asafa Powell'),
                (9.98, 'Frankie Fredericks'),
                (9.74, 'Justin Gatlin'),
                (9.92, 'Christophe Lemaitre'),
                (9.69, 'Tyson Gay')
             ]

    print(find_best(runners, 5))
    print(find_best_with_sort(runners, 5))