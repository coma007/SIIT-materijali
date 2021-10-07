# v04z02
# Napisati program	za	konverziju pozitivnog celog broja zapisanog u dekadnom sistemu u string	u zadatoj brojnoj
# osnovi uz upotrebu structure podataka Stack

from z01_Stack import Stack

numbers = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


def int_to_str(num, base):

    stack = Stack()
    while num != 0:
        rest = num % base
        num //= base
        stack.push(numbers[rest])

    string = ""
    while not stack.is_empty():
        string += stack.pop()

    return string


if __name__ == '__main__':

    n = eval(input("\nInput decimal integer: "))
    b = eval(input("Input base (2-16): "))

    print(f"\nNumber {n} in {b} base system is {int_to_str(n,b)}")
