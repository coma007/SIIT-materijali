from sys import getrefcount

def inc(i):
    i += 1
    return i

def increment_example():
    print("=" * 25)
    print("INCREMENT EXAMPLE".center(25))
    print("=" * 25)
    i = 0
    print("Before inc: i =", i)
    inc(i)
    print("After inc : i =", i)
    print("=" * 25)

def sum(num1, num2):
    z = num1 + num2
    return z

def sum_example():
    print("\n"*2 + "=" * 25)
    print("SUM EXAMPLE".center(25))
    print("=" * 205)

    a = 3
    b = 4

    print("\tBefore: a =",a)
    print("\t\t\tb =", b)

    c = sum(a, b)

    print("\tAfter:  a =",a)
    print("\t\t\tb =", b)
    print("\t\t\tc =", c)
    print("=" * 25)

def add_letter(str):
    str += "D"

def string_example():
    print("\n"*2 + "=" * 25)
    print("STRING EXAMPLE".center(25))
    print("=" * 25)

    str1 = "ABC"

    print("\tBefore: str1 =", str1)

    add_letter(str1)

    print("\tAfter:  str1 =", str1)
    print("=" * 25)


def immutable_types_example():
    increment_example()
    sum_example()

def add_to_list(list):
    list.append(1000)

def list_example():
    my_list = [1, 2, 3]
    add_to_list(my_list)
    print(my_list)

def mutable_types_example():
    list_example()

def refcount_example():
    print(getrefcount(3))
    a = 3
    print(getrefcount(3))

if __name__ == '__main__':
    string_example()
    #immutable_types_example()
    #mutable_types_example()
    refcount_example()