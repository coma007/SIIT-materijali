package rs.ac.uns.ftn.informatika.jpa.controller;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import rs.ac.uns.ftn.informatika.jpa.dto.CourseDTO;
import rs.ac.uns.ftn.informatika.jpa.dto.ExamDTO;
import rs.ac.uns.ftn.informatika.jpa.dto.StudentDTO;
import rs.ac.uns.ftn.informatika.jpa.model.Course;
import rs.ac.uns.ftn.informatika.jpa.model.Exam;
import rs.ac.uns.ftn.informatika.jpa.service.CourseService;

@RestController
@RequestMapping(value = "api/courses")
public class CourseController {

	@Autowired
	private CourseService courseService;

	@GetMapping
	public ResponseEntity<List<CourseDTO>> getCourses() {

		List<Course> courses = courseService.findAll();

		// convert courses to DTOs
		List<CourseDTO> coursesDTO = new ArrayList<>();
		for (Course s : courses) {
			coursesDTO.add(new CourseDTO(s));
		}

		return new ResponseEntity<>(coursesDTO, HttpStatus.OK);
	}

	@GetMapping(value = "/{id}")
	public ResponseEntity<CourseDTO> getCourse(@PathVariable Integer id) {

		Course course = courseService.findOne(id);

		// course must exist
		if (course == null) {
			return new ResponseEntity<>(HttpStatus.NOT_FOUND);
		}

		return new ResponseEntity<>(new CourseDTO(course), HttpStatus.OK);
	}

	@PostMapping(consumes = "application/json")
	public ResponseEntity<CourseDTO> saveCourse(@RequestBody CourseDTO courseDTO) {

		Course course = new Course();
		course.setName(courseDTO.getName());

		course = courseService.save(course);
		return new ResponseEntity<>(new CourseDTO(course), HttpStatus.CREATED);
	}

	@PutMapping(consumes = "application/json")
	public ResponseEntity<CourseDTO> updateCourse(@RequestBody CourseDTO courseDTO) {

		// a course must exist
		Course course = courseService.findOne(courseDTO.getId());

		if (course == null) {
			return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
		}

		course.setName(courseDTO.getName());

		course = courseService.save(course);
		return new ResponseEntity<>(new CourseDTO(course), HttpStatus.OK);
	}

	@DeleteMapping(value = "/{id}")
	public ResponseEntity<Void> deleteCourse(@PathVariable Integer id) {

		Course course = courseService.findOne(id);

		if (course != null) {
			courseService.remove(id);
			return new ResponseEntity<>(HttpStatus.OK);
		} else {
			return new ResponseEntity<>(HttpStatus.NOT_FOUND);
		}
	}

	@GetMapping(value = "/{courseId}/exams")
	public ResponseEntity<List<ExamDTO>> getStudentExams(@PathVariable Integer courseId) {

		Course course = courseService.findOneWithExams(courseId);

		Set<Exam> exams = course.getExams();
		List<ExamDTO> examsDTO = new ArrayList<>();

		for (Exam e : exams) {
			ExamDTO examDTO = new ExamDTO();
			examDTO.setId(e.getId());
			examDTO.setGrade(e.getGrade());
			examDTO.setDate(e.getDate());
			examDTO.setStudent(new StudentDTO(e.getStudent()));
			examDTO.setCourse(new CourseDTO(course));

			examsDTO.add(examDTO);
		}

		return new ResponseEntity<>(examsDTO, HttpStatus.OK);
	}
}
