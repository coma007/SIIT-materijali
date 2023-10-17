package rs.ac.uns.ftn.informatika.jpa.dto;

import java.time.LocalDate;

import rs.ac.uns.ftn.informatika.jpa.model.Exam;

public class ExamDTO {
	private Integer id;
	private Integer grade;
	private LocalDate date;
	private CourseDTO course;
	private StudentDTO student;

	public ExamDTO() {

	}

	public ExamDTO(Exam exam) {
		id = exam.getId();
		grade = exam.getGrade();
		date = exam.getDate();
		course = new CourseDTO(exam.getCourse());
		student = new StudentDTO(exam.getStudent());
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

	public CourseDTO getCourse() {
		return course;
	}

	public void setCourse(CourseDTO course) {
		this.course = course;
	}

	public StudentDTO getStudent() {
		return student;
	}

	public void setStudent(StudentDTO student) {
		this.student = student;
	}
}
