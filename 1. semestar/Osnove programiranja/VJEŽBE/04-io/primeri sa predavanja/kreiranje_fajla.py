if __name__=='__main__':
    test_file = open("test_file.txt", "w")

    for i in range(5):
        name = input("Unesi ime:")
        test_file.write(name + "\n")

    test_file.close()
