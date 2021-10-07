import random
import time


def bubble_sort(array):
    n = len(array)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def selection_sort(array):
    for i in range(len(array)-1, 0, -1):
        maxpos = 0
        for j in range(1, i+1):
            if array[j] > array[maxpos]:
                maxpos = j
        array[i], array[maxpos] = array[maxpos], array[i]


def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        pos = i
        while pos > 0 and array[pos-1] > current:
            array[pos] = array[pos-1]
            pos = pos - 1
        array[pos] = current


def heap_sort(array):
    for start in range((len(array)-2)//2, -1, -1):
        _siftdown(array, start, len(array)-1)
 
    for end in range(len(array)-1, 0, -1):
        array[end], array[0] = array[0], array[end]
        _siftdown(array, 0, end - 1)
    return array


def _siftdown(array, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break


def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i+1
            else:
                array[k]=righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j+1
            k = k+1


def quick_sort(array):
    _quick_sort(array, 0, len(array)-1)


def _quick_sort(array, first, last):
    if first < last:
        splitpoint = _partition(array, first, last)
        _quick_sort(array, first, splitpoint-1)
        _quick_sort(array, splitpoint+1, last)


def _partition(array, first, last):
    pivotvalue = array[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and array[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while array[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            temp = array[leftmark]
            array[leftmark] = array[rightmark]
            array[rightmark] = temp
    temp = array[first]
    array[first] = array[rightmark]
    array[rightmark] = temp
    return rightmark


def bucket_sort(array):
    """Pretpostavlja da je array niz integera sa vrednostima 0...len(array)-1"""
    buckets = [None] * len(array)
    for elem in array:
        buckets[elem] = elem
    return buckets


def test_run(name, func, array):
    random.shuffle(array)
    start = time.process_time()
    func(array)
    end = time.process_time()
    print("%-20s %10f" % (name, end-start))


def generate_collection_and_test(number_of_elements):
    print("Pokrećemo algoritme sortiranja za kolekciju od", number_of_elements, "elemenata")
    print("=" * 70)

    test_array = [_ for _ in range(number_of_elements)]
    test_run("Bubble sort", bubble_sort, test_array)
    test_run("Selection sort", selection_sort, test_array)
    test_run("Insertion sort", insertion_sort, test_array)
    test_run("Heap sort", heap_sort, test_array)
    test_run("Merge sort", merge_sort, test_array)
    test_run("Quick sort", quick_sort, test_array)
    test_run("Bucket sort", bucket_sort, test_array)

    print("=" * 70 + "\n\n")


if __name__ == '__main__':
    generate_collection_and_test(1000)

    generate_collection_and_test(10000)

    generate_collection_and_test(100000)
