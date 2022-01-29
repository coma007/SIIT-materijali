def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

if __name__ == '__main__':

    gen = my_range(2)
    print(gen)
    try:
        while True:
            print(next(gen))
    except StopIteration:
        print("Generisani su svi elementi.")

