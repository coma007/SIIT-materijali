if __name__ == '__main__':
    test_file = open("test_file.txt", "a")

    name = input("Unesi ime:")
    test_file.write(name + "\n")

    test_file.close()
