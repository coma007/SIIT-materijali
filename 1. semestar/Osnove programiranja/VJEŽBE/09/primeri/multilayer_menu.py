def option1():
    print("Odabrali ste opciju 1")

def option2():
    print("Odabrali ste opciju 2")

def option3():
    print("Odabrali ste opciju 3")

def option4():
    print("Odabrali ste opciju 4")

def back():
    print("Odabrali ste opciju za povratak")

def izlaz():
    print("Odabrali ste opciju za izlazak iz aplikacije.")

def submenu2():

    submenu2_dict = {
        '4': option4,
        'b': back
    }

    while True:
        print("=" * 30)
        print("Odabrali ste podmeni 2")
        print("=" * 30)
        print("Ponuđene opcije:")
        print("4. Opcija 4\nb. Povratak na prethodni meni")
        user_input = input(">>")

        if user_input in submenu2_dict:
            submenu2_dict[user_input]()
            if user_input == 'b':
                return
        else:
            print("Odabrali ste nepostojeću opciju")

def submenu1():

    submenu1_dict = {
        '1': option1,
        '2': option2,
        '3': submenu2,
        'b': back
    }

    while True:
        print("=" * 30)
        print("Odabrali ste podmeni 1")
        print("=" * 30)
        print("Ponuđene opcije:")
        print("1. Opcija 1\n2. Opcija 2\n3. Podmeni 2\nb. Povratak na prethodni meni")

        user_input = input(">>")

        if user_input in submenu1_dict:
            submenu1_dict[user_input]()
            if user_input == 'b':
                return
        else:
            print("Odabrali ste nepostojeću opciju")

def menu():

    menu_dict = {
        '1': submenu1,
        '2': submenu2,
        '3': option3,
        'x': izlaz
    }

    while True:
        print("=" * 30)
        print("Glavni meni aplikacije")
        print("=" * 30)
        print("Ponuđene opcije:")
        print("1. Podmeni 1\n2. Podmeni 2\n3. Opcija 3\nx. Izlaz")

        user_input = input(">>")

        if user_input in menu_dict:
            menu_dict[user_input]()
            if user_input == 'x':
                return
        else:
            print("Odabrali ste nepostojeću opciju")


if __name__ == '__main__':
    menu()
