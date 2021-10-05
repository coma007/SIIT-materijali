def input_exceptions():
    str_broj = input("Unesite broj:")
    while True:
        try:
            broj = eval(str_broj)
            print("Uneli ste broj", broj)
            break
        except NameError as exc:
            print(exc)
        except Exception as ie:
            print(ie)


def deljenje(prvi, drugi):
    if drugi != 0:
        return prvi/drugi
    raise ZeroDivisionError("Deljenje nulom nije dozvoljeno.")


def main():
    try:
        print(deljenje(1, 0))
    except Exception as zde:
        print(zde)

if __name__ == '__main__':
    input_exceptions()
    main()
