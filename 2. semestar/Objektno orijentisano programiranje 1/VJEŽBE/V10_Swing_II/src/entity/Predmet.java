package entity;

public class Predmet {
	private int id;
	private String sifra, naziv, semestar;
	
	public Predmet(int id, String sifra, String naziv, String semestar) {
		super();
		this.id = id;
		this.sifra = sifra;
		this.naziv = naziv;
		this.semestar = semestar;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getSifra() {
		return sifra;
	}

	public void setSifra(String sifra) {
		this.sifra = sifra;
	}

	public String getNaziv() {
		return naziv;
	}

	public void setNaziv(String naziv) {
		this.naziv = naziv;
	}

	public String getSemestar() {
		return semestar;
	}

	public void setSemestar(String semestar) {
		this.semestar = semestar;
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
		Predmet other = (Predmet) obj;
		if (id != other.id)
			return false;
		return true;
	}

	@Override
	public String toString() {
		return "Predmet [id=" + id + ", sifra=" + sifra + ", naziv=" + naziv + ", semestar=" + semestar + "]";
	}

	public String toFileString() {
		return id+","+sifra+","+naziv+","+semestar;
	}
	
	
}
