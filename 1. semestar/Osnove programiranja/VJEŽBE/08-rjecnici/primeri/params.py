# kwargs, args, named params

def create_person_dict(first_name,  last_name):
    return {"first_name": first_name, "last_name": last_name}

# kwargs example
# person has first_name and last_name along with additional attributes
def create_person_dict_with_kwargs(first_name,  last_name, **kwargs):
    person = create_person_dict(first_name,  last_name)
    for key in kwargs:
        person[key] = kwargs[key]

    return person

# args example
def sumiraj(*args):
    suma = 0

    for arg in args:
        suma += arg
    return suma


if __name__ == '__main__':
    print(create_person_dict_with_kwargs("Sima", "Simic", id=11, height=184))
    # ili
    # print(create_person_dict_with_kwargs(first_name="Sima", last_name="Simic", id=11, heightx=184))
    # ili
    # new_dict = {"id": 11, "height": 184}
    # print(create_person_dict_with_kwargs("Sima", "Simic", **new_dict))

    print(sumiraj(1, 2, 4, 5, 6, 7))
