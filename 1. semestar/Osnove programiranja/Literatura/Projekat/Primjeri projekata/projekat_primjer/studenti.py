# studenti.py

from os.path import exists

def loadStudents():
    checkFile()
    for line in open('studenti.txt', 'r').readlines():
        if len(line) > 1:
            stud = str2student(line)
            studenti.append(stud)

def saveStudents():
    file = open('studenti.txt', 'w')
    for stud in studenti:
        file.write(student2str(stud))
        file.write('\n')
    file.close()
    
def checkFile():
    if not exists('studenti.txt'):
        open('studenti.txt', 'w').close()

def findStudent(indeks):
    for stud in studenti:
        if stud['indeks'] == indeks:
            return stud
    return None
    
def searchStudents(field, value):
    result = []
    for stud in studenti:
        if stud[field].upper() == value.upper():
            result.append(stud)
    return result

def addStudent(stud):
    studenti.append(stud)

def updateStudent(index, stud):
    studenti[index] = stud

def advanceStudent(stud):
    stud['godina'] = str(int(stud['godina']) + 1)

#def getPos(stud):
#    for i in range(len(studenti)):
#        if stud['indeks'] == studenti[i]['indeks']:
#            return i
#    return -1

def str2student(line):
    if line[-1] == '\n':
        line = line[:-1]
    indeks, ime, prezime, roditelj, datum, jmbg, adresa, telefon, email, godina = line.split('|')
    stud = {
      'indeks': indeks,
      'ime': ime,
      'prezime': prezime,
      'roditelj': roditelj,
      'datum': datum,
      'jmbg': jmbg,
      'adresa': adresa,
      'telefon': telefon,
      'email': email,
      'godina': godina
    }
    return stud

def student2str(stud):
    return '|'.join([stud['indeks'], stud['ime'], stud['prezime'], 
      stud['roditelj'], stud['datum'], stud['jmbg'], stud['adresa'], 
      stud['telefon'], stud['email'], stud['godina']])

def formatHeader():
    return \
      "Indeks  |Ime       |Prezime     |Ime rod.  |Datum rodj.|JMBG         |Email               |Godina\n" \
      "--------+----------+------------+----------+-----------+-------------+--------------------+------"

def formatStudent(stud):
    return u"{0:8}|{1:10}|{2:12}|{3:10}|{4:10}|{5:13}|{6:20}|{7:>6}".format(
      stud['indeks'],
      stud['ime'],
      stud['prezime'],
      stud['roditelj'],
      stud['datum'],
      stud['jmbg'],
      #stud['adresa'],
      #stud['telefon'],
      stud['email'],
      stud['godina'])

def formatStudents(studList):
    result = ""
    for stud in studList:
        result += formatStudent(stud) + '\n'
    return result

def formatAllStudents():
    return formatStudents(studenti)

def findMin(studList, key, start):
    n = len(studList)
    if n == 0:
        return -1
    if n <= start:
        return -1
    if n-start == 1:
        return start
    min = studList[start]
    minPos = start
    for i in range(start+1, n):
        if studList[i][key] < min[key]:
            min = studList[i]
            minPos = i
    return minPos

def sort(studList, key, start):
    minPos = findMin(studList, key, start)
    if minPos == -1:
        return
    studList[start], studList[minPos] = studList[minPos], studList[start]
    if start < len(studList)-1:
        sort(studList, key, start+1)

def sortStudents(key):
    sort(studenti, key, 0)
            
studenti = []
loadStudents()
