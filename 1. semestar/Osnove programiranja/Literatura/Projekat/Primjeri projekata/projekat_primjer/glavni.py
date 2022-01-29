import referenti
import studenti

def main():
    print()
    print("Evidencija studenata")
    print("====================")
    print()
    if not login():
        print("\nNiste uneli postojece ime i lozinku!")
        return
    komanda = '0'
    while komanda != 'X':
        komanda = menu()
        if komanda == '1':
            findStudent()
        elif komanda == '2':
            searchStudents()
        elif komanda == '3':
            listStudents()
        elif komanda == '4':
            updateStudent()
        elif komanda == '5':
            addStudent()
        elif komanda == '6':
            advanceStudents()
    print("Dovidjenja.")

def menu():
    printMenu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        printMenu()
        command = input(">> ")
    return command.upper()

def printMenu():
    print("\nIzaberite opciju:")
    print("  1 - pronalazenje studenta")
    print("  2 - pretrazivanje studenata")
    print("  3 - pregled svih studenata")
    print("  4 - izmena podataka o studentu")
    print("  5 - upis novog studenta")
    print("  6 - upis nove godine studija")
    print("  x - izlaz iz programa")

def login():
    username = input("Korisnicko ime >> ")
    password = input("Lozinka >> ")
    return referenti.login(username, password)

def findStudent():
    print("[1] Pronalazenje studenta\n")
    indeks = input("Unesite broj indeksa >> ")
    stud = studenti.findStudent(indeks)
    if stud != None:
        print(studenti.formatHeader())
        print(studenti.formatStudent(stud))
    else:
        print("Nije pronadjen student sa brojem indeksa", indeks)

def searchStudents():
    print("[2] Pretrazivanje studenata\n")
    prezime = input("Unesite prezime >> ")
    studList = studenti.searchStudents('prezime', prezime)
    if len(studList) == 0:
        print("\nNema trazenih studenata.")
    else:
        print('\n')
        print(studenti.formatHeader())
        print(studenti.formatStudents(studList))

def listStudents():
    print("[3] Pregled svih studenata sortiranih po prezimenu\n")
    studenti.sortStudents('prezime')
    print(studenti.formatHeader())
    print(studenti.formatAllStudents())
    
def updateStudent():
    print("[4] Izmena podataka o studentu\n")
    indeks = input("Unesite broj indeksa >> ")
    stud = studenti.findStudent(indeks)
    if stud == None:
        print("Ne postoji student sa datim brojem indeksa.")
    else:
        print(studenti.formatHeader())
        print(studenti.formatStudent(stud))
        stud['adresa'] = input("Unesite adresu studenta >> ")
        stud['telefon'] = input("Unesite telefon studenta >> ")
        stud['email'] = input("Unesite e-mail studenta >> ")
        studenti.saveStudents()

def addStudent():
    print("[5] Upis novog studenta\n")
    stud = {}
    stud['indeks'] = input("Unesite indeks >> ")
    stud['ime'] = input("Unesite ime >> ")
    stud['prezime'] = input("Unesite prezime >> ")
    stud['roditelj'] = input("Unesite ime roditelja >> ")
    stud['datum'] = input("Unesite datum rodjenja >> ")
    stud['jmbg'] = input("Unesite JMBG >> ")
    stud['adresa'] = input("Unesite adresu >> ")
    stud['telefon'] = input("Unesite telefon >> ")
    stud['email'] = input("Unesite e-mail >> ")
    stud['godina'] = '1'
    studenti.addStudent(stud)
    studenti.saveStudents()
    
def advanceStudents():
    print("[6] Upis studenata u narednu godinu studija\n")
    indeks = input("Unesite indeks studenta koji upisuje narednu godinu (<Enter> za kraj) >> ")
    while indeks != '':
        stud = studenti.findStudent(indeks)
        if stud == None:
            print("Ne postoji student sa datim brojem indeksa.")
        else:
            studenti.advanceStudent(stud)
            print("Student", indeks, "je upisan u narednu godinu.")
        indeks = input("Unesite indeks studenta koji upisuje narednu godinu (<Enter> za kraj) >> ")
    studenti.saveStudents()
    
if __name__ == '__main__':
    main()
