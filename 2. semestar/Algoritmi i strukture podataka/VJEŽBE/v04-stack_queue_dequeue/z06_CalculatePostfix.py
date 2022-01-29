# v04z06
# Napisati program za izračunavanje vrednosti izraza zapisanog u postfiksnoj notaciji uz upotrebu implementirane klase Stack.

from z01_Stack import Stack

operations = "+-*/"


def calculate(postfix):

    stack = Stack()

    result = 0
    for char in postfix:
        if not char.isdigit() and char not in operations:
            continue
        elif char.isdigit():
            stack.push(char)
        elif char in operations:
            num2 = stack.pop()
            operator = char
            num1 = stack.pop()
            result = eval(num1 + operator + num2)
            stack.push(str(result))

    result = stack.pop()
    return result


if __name__ == '__main__':

    string = "3 2 +"
    print("Postfix: " + string + "\nResult: " + calculate(string) + "\n")
    string = " 3	2	*"
    print("Postfix: " + string + "\nResult: " + calculate(string) + "\n")
    string = "4 3 * 9 +"
    print("Postfix: " + string + "\nResult: " + calculate(string) + "\n")
    string = "7 3 2 * -"
    print("Postfix: " + string + "\nResult: " + calculate(string) + "\n")
    string = "2 3 + 7 *"
    print("Postfix: " + string + "\nResult: " + calculate(string) + "\n")
    string = "8 4 1 3 + * 2 / 1 - -"
    print("Postfix: " + string + "\nResult: " + calculate(string) + "\n")
