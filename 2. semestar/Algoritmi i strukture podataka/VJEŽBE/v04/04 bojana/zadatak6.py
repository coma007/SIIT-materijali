"""
Program izračunava vrednost izraza u postfiksnoj notaciji.
"""
from stack import Stack

OPERANDS = "0123456789"


def calculate(operator, a, b):
    """
    Funkcija izračunava vrednost izraza.

    Argumenti:
    - `operator`: zadati binarni operator
    - `a`: prvi operand
    - `b`: drugi operand
    """
    if operator == '*':
        return a*b
    elif operator == '/':
        return b/a
    elif operator == '+':
        return a+b
    else:
        return b-a


def evaluate(postfix):
    """
    Funkcija izračunava vrednost izraza u postfiksnoj notaciji.

    Argument:
    - `postfix`: zadati izraz
    """
    operands = Stack()

    tokens = postfix.split()
    for token in tokens:
        if token in OPERANDS:
            # operandi se smeštaju na stek
            operands.push(int(token))
        else:
            # operandi se skidaju sa steka za svaki operator
            first = operands.pop()
            second = operands.pop()

            # izračunava se rezultat operacije i smešta se na stek
            result = calculate(token, first, second)
            operands.push(result)

    # nakon prolaza kroz niz tokena jedini element na steku je rezultat
    return operands.pop()


if __name__ == '__main__':
    print(evaluate('7 8 + 3 2 + /'))
    print(evaluate('6 2 /'))
    print(evaluate('9 6 -'))
