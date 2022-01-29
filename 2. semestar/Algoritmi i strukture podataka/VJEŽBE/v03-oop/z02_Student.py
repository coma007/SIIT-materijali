# v03z02
# Proširiti klasu Student iz primera da	podrži evidentiranje ocena i ispis proseka.

class Student(object):

    def __init__(self, firstname, lastname, grades=None):
        self._firstname = firstname
        self._lastname = lastname
        if grades is not None:
            self._grades = grades
        else:
            self._grades = []

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        self._firstname = firstname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    def add_grade(self, grade):
        self._grades.append(grade)
        print(f"Grade {grade} added !")
        self.gpa()

    def annul_grade(self, annul):
        for grade in self._grades:
            if grade == annul:
                self._grades.remove(grade)
                print(f"Grade {grade} annuled !")
                break
        else:
            print(f"Grade {annul} not found !")
        self.gpa()

    def gpa(self):
        gpa = 0
        for grade in self._grades:
            gpa += grade
        gpa /= len(self._grades)
        print("Student's GPA: ", gpa)
        return gpa

    def introduce_yourself(self):
        return "Ja sam " + self._firstname + " " + self._lastname


if __name__ == '__main__':

    student1 = Student("Student", "Student")
    print(student1.introduce_yourself(), "\n")
    student1.add_grade(10)
    student1.add_grade(10)
    student1.add_grade(10)
    student1.add_grade(9)
    student1.annul_grade(9)
    student1.add_grade(10)
    student1.add_grade(10)

    print("\n")
    student2 = Student("Studentica", "Studentica", grades=[9, 10, 10, 9, 10])
    print(student2.introduce_yourself(), "\n")
    student2.gpa()
