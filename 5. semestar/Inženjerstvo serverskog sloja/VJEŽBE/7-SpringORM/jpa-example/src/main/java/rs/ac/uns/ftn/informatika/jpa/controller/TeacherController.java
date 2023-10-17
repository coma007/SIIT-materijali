package rs.ac.uns.ftn.informatika.jpa.controller;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import rs.ac.uns.ftn.informatika.jpa.dto.CourseDTO;
import rs.ac.uns.ftn.informatika.jpa.dto.TeacherDTO;
import rs.ac.uns.ftn.informatika.jpa.mapper.TeacherDTOMapper;
import rs.ac.uns.ftn.informatika.jpa.model.Course;
import rs.ac.uns.ftn.informatika.jpa.model.Teacher;
import rs.ac.uns.ftn.informatika.jpa.service.TeacherService;

@RestController
@RequestMapping(value = "api/teachers")
public class TeacherController {

	@Autowired
	private TeacherService teacherService;

	@GetMapping(value = "/all")
	public ResponseEntity<List<TeacherDTO>> getAllTeachers() {

		List<Teacher> teachers = teacherService.findAll();

		// convert teachers to DTOs
		List<TeacherDTO> teachersDTO = new ArrayList<>();
		for (Teacher s : teachers) {
			teachersDTO.add(new TeacherDTO(s));
		}

		return new ResponseEntity<>(teachersDTO, HttpStatus.OK);
	}

	@GetMapping
	public ResponseEntity<List<TeacherDTO>> getTeachersPage(Pageable page) {

		Page<Teacher> teachers = teacherService.findAll(page);

		// convert teachers to DTOs
		List<TeacherDTO> teachersDTO = teachers.stream()
									.map(TeacherDTOMapper::fromTeachertoDTO)
									.collect(Collectors.toList());

		return new ResponseEntity<>(teachersDTO, HttpStatus.OK);
	}

	@GetMapping(value = "/{id}")
	public ResponseEntity<TeacherDTO> getTeacher(@PathVariable Integer id) {

		Teacher teacher = teacherService.findOne(id);

		if (teacher == null) {
			return new ResponseEntity<>(HttpStatus.NOT_FOUND);
		}

		return new ResponseEntity<>(new TeacherDTO(teacher), HttpStatus.OK);
	}

	@PostMapping(consumes = "application/json")
	public ResponseEntity<TeacherDTO> saveTeacher(@RequestBody TeacherDTO teacherDTO) {

		Teacher teacher = new Teacher();
		teacher.setFirstName(teacherDTO.getFirstName());
		teacher.setLastName(teacherDTO.getLastName());

		teacher = teacherService.save(teacher);
		return new ResponseEntity<>(new TeacherDTO(teacher), HttpStatus.CREATED);
	}

	@PutMapping(consumes = "application/json")
	public ResponseEntity<TeacherDTO> updateTeacher(@RequestBody TeacherDTO teacherDTO) {

		// a teacher must exist
		Teacher teacher = teacherService.findOne(teacherDTO.getId());

		if (teacher == null) {
			return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
		}

		teacher.setFirstName(teacherDTO.getFirstName());
		teacher.setLastName(teacherDTO.getLastName());

		teacher = teacherService.save(teacher);
		return new ResponseEntity<>(new TeacherDTO(teacher), HttpStatus.OK);
	}

	@DeleteMapping(value = "/{id}")
	public ResponseEntity<Void> deleteTeacher(@PathVariable Integer id) {

		Teacher teacher = teacherService.findOne(id);

		if (teacher != null) {
			teacherService.remove(id);
			return new ResponseEntity<>(HttpStatus.OK);
		} else {
			return new ResponseEntity<>(HttpStatus.NOT_FOUND);
		}
	}

	@GetMapping(value = "/{teacherId}/courses")
	public ResponseEntity<List<CourseDTO>> getTeacherCourses(@PathVariable Integer teacherId) {

		Teacher teacher = teacherService.findOneWithCourses(teacherId);

		Set<Course> courses = teacher.getCourses();
		List<CourseDTO> coursesDTO = new ArrayList<>();

		for (Course c : courses) {
			coursesDTO.add(new CourseDTO(c));
		}
		return new ResponseEntity<>(coursesDTO, HttpStatus.OK);
	}
	
	@GetMapping(value = "/checkDeleted")
	public ResponseEntity<List<TeacherDTO>> getDeletedTeachers(@RequestParam boolean deleted) {
		List<Teacher> teachers = new ArrayList<Teacher>();
		
		if (deleted) {
			teachers = teacherService.findAllDeleted();
		} else {
			teachers = teacherService.findAll();
		}

		List<TeacherDTO> teachersDTO = teachers.stream()
				.map(TeacherDTOMapper::fromTeachertoDTO)
				.collect(Collectors.toList());
		
		return new ResponseEntity<>(teachersDTO, HttpStatus.OK);
	}
}
