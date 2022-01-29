if __name__ == '__main__':
    test_file = open("test_file.txt", "r")

    print(test_file.readline())
    print(test_file.readline())
    print(test_file.readline())
    print(test_file.readline())
    print(test_file.readline())
    print(test_file.readline())
    print(test_file.readline())

    test_file.close()
