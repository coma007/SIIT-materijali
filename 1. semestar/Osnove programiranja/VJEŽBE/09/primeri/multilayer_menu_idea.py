menus = {}

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

def execute_menu(menu_reference):
    menu = menus[menu_reference]
    while True:
        print("=" * 30)
        print("Odabrali ste", menu["pretty_name"])
        print("=" * 30)
        print("Ponuđene opcije:")
        print(menu["options_text"])

        user_input = input(">>")

        if user_input in menu["options_dict"]:
            function_to_call = menu["options_dict"][user_input]
            if menu["options_dict"][user_input] not in menus:
                function_to_call()
            else:
                execute_menu(function_to_call)

            if menu["back_allowed"] and user_input == 'b':
                return
            if menu["exit_allowed"] and user_input == 'x':
                exit()
        else:
            print("Odabrali ste nepostojeću opciju")

def submenu2():

    submenu2_dict = {
        '4': option4,
        'b': back
    }

    submenu_options_dict = {
        'name': "submenu2",
        'pretty_name': "Podmeni 2",
        'options_text': "4. Opcija 4\nb. Povratak na prethodni meni",
        'options_dict': submenu2_dict,
        'back_allowed': True,
        'exit_allowed': False
    }

    menus[submenu2] = submenu_options_dict

def submenu1():

    submenu1_dict = {
        '1': option1,
        '2': option2,
        '3': submenu2,
        'b': back
    }

    submenu_options_dict = {
        'name': "submenu1",
        'pretty_name': "Podmeni 1",
        'options_text': "1. Opcija 1\n2. Opcija 2\n3. Podmeni 2\nb. Povratak na prethodni meni",
        'options_dict': submenu1_dict,
        'back_allowed': True,
        'exit_allowed': False
    }

    menus[submenu1] = submenu_options_dict

def menu():

    menu_dict = {
        '1': submenu1,
        '2': submenu2,
        '3': option3,
        'x': izlaz
    }

    menu_options_dict = {
        'name': "menu",
        'pretty_name': "glavni meni aplikacije",
        'options_text': "1. Podmeni 1\n2. Podmeni 2\n3. Opcija 3\nx. Izlazak iz aplikacije",
        'options_dict': menu_dict,
        'back_allowed': False,
        'exit_allowed': True
    }

    menus[menu] = menu_options_dict

def initiate():
    menu()
    submenu1()
    submenu2()

if __name__ == '__main__':
    initiate()
    execute_menu(menu)
