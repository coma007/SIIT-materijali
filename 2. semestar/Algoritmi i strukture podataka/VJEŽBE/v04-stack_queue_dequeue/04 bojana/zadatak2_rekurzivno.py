"""
Program vrši konverziju broja iz dekadnog brojnog sistema u zadatu brojnu osnovu
na intervalu [2, 16].
"""
from stack import Stack

# moguće cifre na zadatom intervalu
DIGITS = "0123456789ABCDEF"

def convert(num, radix, stack):
    if num < radix:
        stack.push(DIGITS[num])

    else:
        stack.push(DIGITS[num % radix])
        return convert(num//radix, radix, stack)


if __name__ == '__main__':
    num = input('Unesi broj: ')
    radix = input('Unesi osnovu: ')
    stack = Stack()
    convert(num, radix, stack)
    output = ''
    while not stack.is_empty():
        output += stack.pop()

    print(output)