package rs.ac.uns.ftn.informatika.jpa.dto;

import rs.ac.uns.ftn.informatika.jpa.model.Teacher;

public class TeacherDTO {
	private Integer id;
	private String firstName;
	private String lastName;

	public TeacherDTO() {

	}

	public TeacherDTO(Teacher teacher) {
		this(teacher.getId(), teacher.getFirstName(), teacher.getLastName());
	}

	public TeacherDTO(Integer id, String firstName, String lastName) {
		super();
		this.id = id;
		this.firstName = firstName;
		this.lastName = lastName;
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
}
