"""
Program vrši konverziju izraza iz infiksne u postfiksnu notaciju.
"""
from stack import Stack

OPERANDS = "0123456789"


def to_postfix(infix):
    """
    Funkcija vrši konverziju izraza iz infiksne u postfiksnu notaciju.

    Argument:
    - `infix`: zadati izraz
    """
    # prioriteti operatora
    priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}

    postfix = []
    operators = Stack()

    for token in infix:
        if token in OPERANDS:
            # operandi se beleže u izlazni bafer
            postfix.append(token)
        elif token == '(':
            # leve zagrade dodaju se na stek
            operators.push(token)
        elif token == ')':
            # ako je token desna zagrada, izbaci sve sa steka do prve leve
            top = operators.pop()
            while top != '(':
                postfix.append(top)
                top = operators.pop()
        else:
            # operatori se dodaju na stek, ali se najpre svi "stariji" izbacuju
            while not operators.is_empty() and \
                  priority[operators.top()] >= priority[token]:
                postfix.append(operators.pop())
            operators.push(token)

    # generisanje rezultujućeg izraza
    while not operators.is_empty():
        postfix.append(operators.pop())
    return " ".join(postfix)


if __name__ == '__main__':
    print(to_postfix('(7+8)/(3+2)'))
    print(to_postfix('9*2-3+5'))
    print(to_postfix('(3+8)*4-(7-1)*(6+6)'))
    print(to_postfix('8-(4*(1+3)/2-11)'))
