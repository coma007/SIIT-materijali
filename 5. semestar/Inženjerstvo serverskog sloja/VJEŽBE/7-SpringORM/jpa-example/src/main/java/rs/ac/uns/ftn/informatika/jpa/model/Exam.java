package rs.ac.uns.ftn.informatika.jpa.model;

import java.time.LocalDate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;

@Entity
public class Exam {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer id;

	@Column(name = "grade", nullable = false)
	private Integer grade;

	@Column(name = "date", nullable = false)
	private LocalDate date;

	//fetchtype EAGER je los za performanse, te ga treba koristiti samo kada je to neophodno
	@ManyToOne(fetch = FetchType.EAGER)
	@JoinColumn(name = "course_id")
	private Course course;

	/*
	 * Druga strana bidirekcione veze 1:n
	 */
	@ManyToOne(fetch = FetchType.EAGER)
	@JoinColumn(name = "student_id")
	private Student student;
	
	public Exam() {
		
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public Integer getGrade() {
		return grade;
	}

	public void setGrade(Integer grade) {
		this.grade = grade;
	}

	public LocalDate getDate() {
		return date;
	}

	public void setDate(LocalDate date) {
		this.date = date;
	}

	public Course getCourse() {
		return course;
	}

	public void setCourse(Course course) {
		this.course = course;
	}

	public Student getStudent() {
		return student;
	}

	public void setStudent(Student student) {
		this.student = student;
	}
	
	@Override
	public boolean equals(Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		Exam e = (Exam) o;
		return id != null && id.equals(e.getId());
	}

	@Override
	public int hashCode() {
		return 1337;
	}

	@Override
	public String toString() {
		return "Exam [id=" + id + ", grade=" + grade + ", date=" + date + "]";
	}
	
	
}
