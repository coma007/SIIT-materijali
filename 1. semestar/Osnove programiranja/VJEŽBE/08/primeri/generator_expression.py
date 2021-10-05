if __name__ == '__main__':
    old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gen_exp = (i**2 for i in old_list if i % 2 == 0)

    for i in gen_exp:
        print(i)