# v03z03
# Implementirati korisničke uloge iz projekta sa predmeta Osnove
# programiranja.
# Implementirati klase:
# • Korisnik,
# • RegistrovaniKlijent,
# • Kozmetičar,
# • Recepcioner,
# • Menadžer

class User(object):

    def __init__(self, username, password, f_name, l_name):
        self._username = username
        self._password = password
        self._f_name = f_name
        self._l_name = l_name
        print(f"User {f_name} {l_name} registered !")

    @property
    def f_name(self):
        return self._f_name

    @f_name.setter
    def f_name(self, firstname):
        self._f_name = firstname

    @property
    def l_name(self):
        return self._l_name

    @l_name.setter
    def l_name(self, lastname):
        self._l_name = lastname

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    def __str__(self):
        return self._f_name + " " + self._l_name


class RegisteredUser(User):

    def __init__(self, username, password, firstname, lastname, phone, mail, gender):
        super().__init__(username, password, firstname, lastname)
        self._phone = phone
        self._mail = mail
        self._gender = gender

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender


class Cosmetician(User):

    def __init__(self, username, password, firstname, lastname, treatments=None):
        super().__init__(username, password, firstname, lastname)
        self._role = "cosmetician"
        if treatments is not None:
            self._treatments = treatments
        else:
            self._treatments = []

    @property
    def treatments(self):
        return self._treatments

    @treatments.setter
    def treatments(self, treatment):
        self._treatments.append(treatment)


class Receptionist(User):

    def __init__(self, username, password, firstname, lastname):
        super().__init__(username, password, firstname, lastname)
        self._role = "receptionist"


class Manager(User):

    def __init__(self, username, password, firstname, lastname, employees=None):
        super().__init__(username, password, firstname, lastname)
        self._role = "manager"
        if employees is None:
            employees = []
        self._employees = employees

    @property
    def employees(self):
        return self._employees

    @employees.setter
    def employees(self, employee):
        self._employees.append(employee)

    def employ(self, employee):
        self._employees.append(employee)

    def fire(self, employee):
        self._employees.remove(employee)


if __name__ == '__main__':

    manager1 = Manager("krinka", "london", "Krinka", "Sladakovic")
    cosmetician1 = Cosmetician("kacamaca", "siit", "Katarina", "Vucic", ["masaza"])
    receptionist1 = Receptionist("mare", "psih", "Marija", "Galic")
    manager1.employ(receptionist1)
    manager1.employ(cosmetician1)
    user1 = RegisteredUser("djole", "mirjana", "Djordje", "Sladakovic", "123123123", "djole@gmail.com", "M")

    print("Manager's employees:")
    for empl in manager1.employees:
        print(empl)
