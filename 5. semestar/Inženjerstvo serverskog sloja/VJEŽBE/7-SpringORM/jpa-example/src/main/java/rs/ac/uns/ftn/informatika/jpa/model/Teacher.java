package rs.ac.uns.ftn.informatika.jpa.model;

import java.util.HashSet;
import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;

import org.hibernate.annotations.SQLDelete;
import org.hibernate.annotations.Where;

/* primer logickog brisanja
 * 
 * Prilikom poziva delete() metode repozitorijuma, okidace se ovaj upit koji radi soft delete
 * tako sto menja status deleted polja sa false na true.
 */
@SQLDelete(sql
	    = "UPDATE teacher "
	    + "SET deleted = true "
	    + "WHERE id = ?")
@Where(clause = "deleted = false")
@Entity
public class Teacher {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer id;

	@Column(name = "firstName", nullable = false)
	private String firstName;

	@Column(name = "lastName", nullable = false)
	private String lastName;
	
	//atribut potreban za logicko brisanje (soft delete)
	//i koji se koristi u @Where klauzuli koju Hibernate dodaje pri svakom upitu koji treba da vrati sve neobrisane torke
	@Column(name = "deleted")
	private boolean deleted;

	@ManyToMany(cascade = {CascadeType.PERSIST,CascadeType.MERGE,CascadeType.DETACH})
	@JoinTable(name = "teaching", joinColumns = @JoinColumn(name = "course_id", referencedColumnName = "id"), inverseJoinColumns = @JoinColumn(name = "teacher_id", referencedColumnName = "id"))
	private Set<Course> courses = new HashSet<Course>();
	
	public Teacher() {
		
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public Set<Course> getCourses() {
		return courses;
	}

	public void setCourses(Set<Course> courses) {
		this.courses = courses;
	}
	
	public boolean isDeleted() {
		return deleted;
	}

	public void setDeleted(boolean deleted) {
		this.deleted = deleted;
	}

	/*
	 * Pri implementaciji equals and hashCode metoda treba obratiti paznju da se
	 * one razlikuju kada se koristi ORM (Hibernate) i kada se klase posmatraju kao
	 * obicne POJO klase. Hibernate zahteva da entitet mora biti jednak samom sebi kroz sva
	 * stanja tog objekta (tranzijentni (novi objekat), perzistentan (persistent), otkacen (detached) i obrisan (removed)).
	 * To znaci da bi dobar pristup bio da se za generisanje equals i hashCode metoda koristi podatak
	 * koji je jedinstven a poznat unapred (tzv. business key) npr. index studenta, isbn knjige, itd.
	 * U slucaju da takvog obelezja nema, obicno se implementacija svodi na proveri da li je id (koji je kljuc) isti.
	 * Posto u velikom broju slucajeva id baza generise, to znaci da u tranzijentnom stanju objekti nisu jednaki.
	 * Postoji nekoliko resenja za ovaj problem:
	 * 1. Naci neko jedinstveno obelezje
	 * 2. Koristiti prirodne kljuceve
	 * 3. Pre cuvanja na neki nacin saznati koja je sledeca vrednost koju ce baza generisati pa pozvati setId metodu da se kompletira objekat cak i pre cuvanja
	 * 4. Na drugi nacin implementirati equals i hashCode - primer u klasi Teacher
	 */
	@Override
	public boolean equals(Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		Teacher t = (Teacher) o;
		return id != null && id.equals(t.getId());
	}

	@Override
	public int hashCode() {
		/*
		 * Pretpostavka je da je u pitanju tranzijentni objekat (jos nije sacuvan u bazu) i da id ima null vrednost.
		 * Kada se sacuva u bazu dobice non-null vrednost. To znaci da ce objekat imati razlicite kljuceve u dva stanja, te ce za generisan
		 * hashCode i equals vratiti razlicite vrednosti. Vracanje konstantne vrednosti resava ovaj problem.
		 * Sa druge strane ovakva implementacija moze da afektuje performanse u slucaju velikog broja objekata
		 * koji ce zavrsiti u istom hash bucket-u.
		 */
		return 1337;
	}

	@Override
	public String toString() {
		return "Teacher [id=" + id + ", firstName=" + firstName + ", lastName=" + lastName + "]";
	}
}
