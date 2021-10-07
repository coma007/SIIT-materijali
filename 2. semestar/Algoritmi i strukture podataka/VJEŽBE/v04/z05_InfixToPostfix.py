# v04z05
# Napisati program	za konverziju izraza iz infiksne u	postfiksnu notaciju uz upotrebu implementacije klase Stack

from z01_Stack import Stack

priority = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}


def conversion(infix):

    stack = Stack()

    postfix = []
    for char in infix:
        if not char.isdigit() and char not in priority:
            continue
        elif char.isdigit():
            postfix.append(char)
        elif char == "(":
            stack.push(char)
        elif char == ")":
            tmp = stack.pop()
            while tmp != "(":
                postfix.append(tmp)
                tmp = stack.pop()
        else:
            while not stack.is_empty() and priority[stack.top()] >= priority[char]:
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return " ".join(postfix)


if __name__ == '__main__':

    string = "3 + 2"
    print("Infix: " + string + "\nPostfix: " + conversion(string) + "\n")
    string = "4 * 3 + 9"
    print("Infix: " + string + "\nPostfix: " + conversion(string) + "\n")
    string = "7-3*2"
    print("Infix: " + string + "\nPostfix: " + conversion(string) + "\n")
    string = " 3 + 4 - 2"
    print("Infix: " + string + "\nPostfix: " + conversion(string) + "\n")
    string = "(2	+	3)	*	7"
    print("Infix: " + string + "\nPostfix: " + conversion(string) + "\n")
    string = "8	- (4	*	(1	+	3)	/	2	- 1)	"
    print("Infix: " + string + "\nPostfix: " + conversion(string) + "\n")
    while True:
        print(conversion(input("input: ")))


