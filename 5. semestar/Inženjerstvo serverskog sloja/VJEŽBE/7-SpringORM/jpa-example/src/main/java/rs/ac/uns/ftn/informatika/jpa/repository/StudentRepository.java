package rs.ac.uns.ftn.informatika.jpa.repository;

import java.util.List;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import rs.ac.uns.ftn.informatika.jpa.model.Student;

/*
 * Primer repozitorijuma u kojem su navedene metode koje po
 * odredjenoj konstrukciji naziva prave upit u bazu.
 * Metode za pretragu pocinju sa find*By* dok u nastavku sadrze
 * nazive atributa iz modela, konkatenirane sa And, Or, Between, LessThan, GreaterThan, Like, itd.
 * uz dodavanje pomocnih uslova poput Containing, AllIgnoringCase, itd.
 */
/*
 * Pri startovanju Spring kontejnera trigerovace se Spring Data
 * infrastruktura koja ce kreirati binove za repozitorijume.
 * Proci se kroz metode navedene u svakom repozitorijumu i
 * pokusati da konstruise upite koji ce se pozivati pri
 * pozivu metoda.
 */

/*
 * Repository je interfejs koji dozvoljava Spring Data infrastrukturi da
 * prepozna korisnicki definisane repozitorijume (alternativa je 
 * da se sam interfejs anotira sa @Repository)
 * CrudRepository dodaje osnovne metode poput cuvanja, brisanja i pronalazenja entiteta
 * PagingAndSortingRepository nasledjuje CrudRepository i dodaje metode
 * za pristup entitetima stranicu po stranicu i njihovo soritiranje
 * JpaRepository nasledjuje PagingAndSortingRepository i dodaje JPA
 * specificne funkcionalnosti poput flush i deleteInBatch.
 * 
 * Razliciti interfejsi koji se mogu iskoristiti dozvoljavaju manipulaciju razlicitim
 * vrstama metoda koje trebaju biti podrzane - npr. repozitorijum treba
 * da bude samo readonly ili treba da ima findAll metodu koja pritom treba
 * da vraca samo deo rezultata ogranicen pomocu Pageable.
 */
public interface StudentRepository extends JpaRepository<Student, Integer> {

	public Student findOneByIndex(String index);

	/*
	 * Pronalazi sve objekte tipa Student i vraca onoliko objekata koliko je
	 * specificirano kroz Pageable objekat. Npr. ako se prosledi objekat: new
	 * PageRequest(0, 10) vratice se nulta stranica sa prvih 10 objekata tipa
	 * Student. Vise informacija na:
	 * http://docs.spring.io/autorepo/docs/spring-data-commons/1.10.0.RC1/api/org/
	 * springframework/data/domain/PageRequest.html
	 */
	public Page<Student> findAll(Pageable pageable);

	/*
	 * Ako se ne navede eksplicitni upit, Spring ce na osnovu imena metode napraviti
	 * isti. Kako name postoji kao atribut klase Student upit koji ce se kreirati za
	 * ovu metodu bi bio: select s from Student s where s.lastName = ?1 uz provere
	 * da li se odgovarajuci atributi nalaze u datoj klasi.
	 */
	public List<Student> findAllByLastName(String lastName);

	/*
	 * Vraca objekat po tacnom imenu i prezimenu ignorisuci mala i velika slova
	 */
	public List<Student> findByFirstNameAndLastNameAllIgnoringCase(String firstName, String lastName);

	/*
	 * Primer eksplicitnog pisanja upita JPQL (Java Persistence Query Language)/ HQL
	 * (Hibernate Query Language) jezikom. Kao rezultat upita vracaju se objekti
	 * tipa Student. Dzoker znacima ?1, ?2, ?3, itd. u upit se ubacuju parametri
	 * metode u redosledu navodjenja. U primeru ?1 ce se zameniti parametrom
	 * prezime.
	 */
	@Query("select s from Student s where s.lastName = ?1")
	public List<Student> pronadjiStudentePoPrezimenu(String prezime);
	
	
	//https://dzone.com/articles/how-to-decide-between-join-and-join-fetch
	@Query("select s from Student s join fetch s.exams e where s.id =?1")
	public Student findOneWithExams(Integer studentId);
}
