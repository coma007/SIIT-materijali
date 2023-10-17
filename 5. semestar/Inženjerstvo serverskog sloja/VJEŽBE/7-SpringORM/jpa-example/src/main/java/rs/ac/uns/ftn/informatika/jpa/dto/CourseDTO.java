package rs.ac.uns.ftn.informatika.jpa.dto;

import rs.ac.uns.ftn.informatika.jpa.model.Course;

public class CourseDTO {
	private Integer id;
	private String name;

	public CourseDTO() {

	}

	public CourseDTO(Course course) {
		this(course.getId(), course.getName());
	}

	public CourseDTO(Integer id, String name) {
		super();
		this.id = id;
		this.name = name;
	}

	public Integer getId() {
		return id;
	}

	public String getName() {
		return name;
	}
}
