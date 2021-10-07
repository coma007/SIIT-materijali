class Person(object):
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @first_name.setter
    def first_name(self, new_value):
        self._first_name = new_value

    @last_name.setter
    def last_name(self, new_value):
        self._last_name = new_value

    def __str__(self):
        return "Person[first_name = " + self._first_name + ", last_name = " + self._last_name + "]"

class User(Person):

    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name)
        self._username = username
        self._password = password
        self._role = "Client"

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_value):
        self._username = new_value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_value):
        self._password = new_value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, new_value):
        self._role = new_value

    def __str__(self):
        return "User[first_name = " + self._first_name + ", last_name = " + self._last_name + ", role = " + self._role + "]"

class RegisteredClient(User):

    def __init__(self, first_name, last_name, username, password, phone, email, gender):
        super().__init__(first_name, last_name, username, password)
        self._phone = phone
        self._email = email
        self._gender = gender

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, new_value):
        self._phone= new_value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_value):
        self._email = new_value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_value):
        self._gender = new_value

class Receptionist(User):

    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name, username, password)
        self.role = "Receptionist"

class Beautician(User):

    def __init__(self, first_name, last_name, username, password, list_of_treatments=None):
        super().__init__(first_name, last_name, username, password)
        self.role = "Beautician"
        if list_of_treatments is None:
            list_of_treatments = []
        self._list_of_treatments = list_of_treatments

    @property
    def list_of_treatments(self):
        return self._list_of_treatments

    def train(self, treatment):
        self._list_of_treatments.append(treatment)

class Manager(User):

    def __init__(self, first_name, last_name, username, password, list_of_employees=None):
        super().__init__(first_name, last_name, username, password)
        self.role = "Manager"
        if list_of_employees is None:
            list_of_employees = []
        self._list_of_employees = list_of_employees

    @property
    def list_of_employees(self):
        return self._list_of_employees

    @list_of_employees.setter
    def list_of_employees(self, new_value):
        self._list_of_employees = new_value

    def employ(self, employee):
        self._list_of_employees.append(employee)

    def fire(self, employee):
        self._list_of_employees.remove(employee)


class Company(object):

    def __init__(self, name, manager=None, employees=None):
        self._name = name
        self._manager = manager
        if manager is not None:
            self._manager.list_of_employees = employees

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        self._name = new_value

    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, new_value):
        self._manager = new_value

    def train_employee(self, training_name, employee):
        if employee.role == "Beautician":
            employee.train(training_name)


if __name__ == '__main__':
    company = Company("MyCompany")
    manager = Manager("Mika", "Mikic", "miki", "123")
    employee1 = Beautician("Jovana", "Jovic", "joka", "123")
    employee2 = Receptionist("Steva", "Stevic", "steva", "123")

    company.manager = manager

    print(manager)

    company.manager.employ(employee1)
    company.manager.employ(employee2)

    for employee in company.manager.list_of_employees:
        print(employee)

    company.manager.fire(employee1)

    for employee in company.manager.list_of_employees:
        print(employee)
        employee.log_in()


