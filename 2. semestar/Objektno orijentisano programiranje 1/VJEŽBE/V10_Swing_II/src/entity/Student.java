package entity;

import java.util.ArrayList;
import java.util.List;

public class Student {
	private int id;
	private String ime, prezime, indeks;
	private List<Predmet> predmeti;
	
	public Student(int id, String ime, String prezime, String indeks) {
		super();
		this.id = id;
		this.ime = ime;
		this.prezime = prezime;
		this.indeks = indeks;
		this.predmeti = new ArrayList<Predmet>();
	}

	public Student(int id, String ime, String prezime, String indeks, List<Predmet> predmeti) {
		super();
		this.id = id;
		this.ime = ime;
		this.prezime = prezime;
		this.indeks = indeks;
		this.predmeti = predmeti;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getIme() {
		return ime;
	}

	public void setIme(String ime) {
		this.ime = ime;
	}

	public String getPrezime() {
		return prezime;
	}

	public void setPrezime(String prezime) {
		this.prezime = prezime;
	}

	public String getIndeks() {
		return indeks;
	}

	public void setIndeks(String indeks) {
		this.indeks = indeks;
	}

	public List<Predmet> getPredmeti() {
		return predmeti;
	}

	public void setPredmeti(List<Predmet> predmeti) {
		this.predmeti = predmeti;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + id;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Student other = (Student) obj;
		if (id != other.id)
			return false;
		return true;
	}

	@Override
	public String toString() {
		return "Student [id=" + id + ", ime=" + ime + ", prezime=" + prezime + ", indeks=" + indeks + "]";
	}
	

	public String toFileString() {
		String ids = "";
		if (this.predmeti != null && this.predmeti.size()>0) {
			for (Predmet p : predmeti) {
				ids +=p.getId()+";";
			}
			ids = ids.substring(0, ids.length()-1);
			ids = ","+ids;
		}
		return id+","+ime+","+prezime+","+indeks+ids;
	}

}
