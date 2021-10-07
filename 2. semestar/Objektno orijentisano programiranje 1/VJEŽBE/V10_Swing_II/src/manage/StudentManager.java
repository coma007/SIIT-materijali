package manage;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import entity.Predmet;
import entity.Student;

public class StudentManager {
	private String studentFile;
	private List<Student> studenti;
	private PredmetManager predmetMng;
	
	public StudentManager(String studentFile, PredmetManager predmetMng) {
		super();
		this.studentFile = studentFile;
		this.predmetMng = predmetMng;
		this.studenti = new ArrayList<Student>();
	}
	
	
	public List<Student> getStudenti() {
		return studenti;
	}


	/** MENI OPCJA ****/
    public void MeniStudentCLI()
    {
    	// U slucaju da se radi projekat sa konzolnim interfejsom
    }

    /** METODE ZA ISPIS OPCIJA ****/
    //ispis teksta osnovnih opcija

    public void IspisiOpcijeStudentaCLI()
    {
    	// U slucaju da se radi projekat sa konzolnim interfejsom
    }

    /** METODE ZA ISPIS STUDENATA i ocena ****/
    //ispisi sve studente
    public void IspisiSveStudenteCLI()
    {
    	// U slucaju da se radi projekat sa konzolnim interfejsom
    }

    /** METODE ZA PRETRAGU STUDENATA****/
    //pronadji studenta
    public Student PronadjiStudentaPoIndeksuCLI()
    {
    	// U slucaju da se radi projekat sa konzolnim interfejsom
        return null;
    }

    //pronadji studenta
    public Student PronadjiStudentaPoIndeksu(String stIndex)
    {
        Student retVal = null;
        for (int i = 0; i < studenti.size(); i++)
        {
        	Student st = studenti.get(i);
            if (st.getIndeks().equals(stIndex))
            {
                retVal = st;
                break;
            }
        }
        return retVal;
    }

    //pronadji studenta
    public Student PronadjiStudentaPoId(int id)
    {
    	Student retVal = null;
        for (int i = 0; i < studenti.size(); i++)
        {
        	Student st = studenti.get(i);
            if (st.getId() == id)
            {
                retVal = st;
                break;
            }
        }
        return retVal;
    }

    public int PronadjiPozicijuStudentaPoIndeksu()
    {

    	return 0;
    }

    /** METODE ZA UNOS i IZMENU STUDENATA****/

    //unos novog studenta
    public void UnosNovogStudentaCLI()
    {
    	// U slucaju da se radi projekat sa konzolnim interfejsom
    }

    //izmena studenta
    public void IzmenaPodatakaOStudentuCLI()
    {
    	// U slucaju da se radi projekat sa konzolnim interfejsom
    }

    //brisanje predmeta
    public void BrisanjePodatakaOStudentuCLI()
    {
    	// U slucaju da se radi projekat sa konzolnim interfejsom
    }
    

    public boolean UkloniStudentaSaPredmeta(Student student, Predmet predmet)
    {
    	// TO DO
       return false;
    }

	public boolean loadData() {
		try {
			BufferedReader br = new BufferedReader(new FileReader(this.studentFile));
			String linija = null;
			while ((linija = br.readLine()) != null) {
				String[] tokeni = linija.split(",");
				Student s = new Student(Integer.parseInt(tokeni[0]), tokeni[1], tokeni[2], tokeni[3]);
				if (tokeni.length > 4) {
					for (String pId : tokeni[4].split(";")) {
						int id = Integer.parseInt(pId);
						s.getPredmeti().add(this.predmetMng.PronadjiPredmetPoId(id));						
					}
				}
				this.studenti.add(s);
			}
			br.close();
		} catch (IOException e) {
			return false;
		}
		return true;
	}
	
	public boolean saveData() {
		PrintWriter pw = null;
		try {
			pw = new PrintWriter(new FileWriter(this.studentFile, false));
			for (Student s : studenti) {
				pw.println(s.toFileString());
			}
			pw.close();
		} catch (IOException e) {
			return false;
		}
		return true;
	}


	public void add(int id, String ime, String prezime, String indeks) {
		this.studenti.add(new Student(id, ime, prezime, indeks));	
		this.saveData();
	}


	public void edit(int id, String ime, String prezime, String indeks) {
		Student s = this.PronadjiStudentaPoId(id);
		s.setIme(ime);
		s.setPrezime(prezime);
		s.setIndeks(indeks);
		this.saveData();
	}


	public void remove(int id) {
		Student s = PronadjiStudentaPoId(id);
		this.studenti.remove(s);
		this.saveData();
	}
}
