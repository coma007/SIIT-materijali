if __name__ == '__main__':

    IN_FILE = "in.txt"

    print("Karakter po karakter:")
    with open(IN_FILE) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            print(c)

    print("\nRed po red:")
    with open(IN_FILE) as f:
        while True:
            l = f.readline()
            if not l:
                break
            print(l)

    print("\nSve odjednom:")
    with open(IN_FILE) as f:
        content = f.read()
        print(content)

    # ispis redova obrnuto u novu datoteku
    with open(IN_FILE) as fin, open("outr.txt", "w") as fout:
        lines = fin.readlines()
        for line in lines[::-1]:
            if line.endswith("\n"):
                fout.write(line)
            else:
                fout.write(line + "\n")

    # ispis karaktera ornuto u novu datoteku
    with open(IN_FILE) as fin, open("outc.txt", "w") as fout:
        content = fin.read()
        fout.write(content[::-1])
