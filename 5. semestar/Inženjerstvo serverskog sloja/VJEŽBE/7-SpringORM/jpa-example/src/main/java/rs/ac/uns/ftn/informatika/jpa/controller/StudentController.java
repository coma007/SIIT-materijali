package rs.ac.uns.ftn.informatika.jpa.controller;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

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
import rs.ac.uns.ftn.informatika.jpa.dto.ExamDTO;
import rs.ac.uns.ftn.informatika.jpa.dto.StudentDTO;
import rs.ac.uns.ftn.informatika.jpa.model.Exam;
import rs.ac.uns.ftn.informatika.jpa.model.Student;
import rs.ac.uns.ftn.informatika.jpa.service.StudentService;

@RestController
@RequestMapping(value = "api/students")
public class StudentController {

	@Autowired
	private StudentService studentService;

	@GetMapping(value = "/all")
	public ResponseEntity<List<StudentDTO>> getAllStudents() {

		List<Student> students = studentService.findAll();

		// convert students to DTOs
		List<StudentDTO> studentsDTO = new ArrayList<>();
		for (Student s : students) {
			studentsDTO.add(new StudentDTO(s));
		}

		return new ResponseEntity<>(studentsDTO, HttpStatus.OK);
	}

	// GET /api/students?page=0&size=5&sort=firstName,DESC
	@GetMapping
	public ResponseEntity<List<StudentDTO>> getStudentsPage(Pageable page) {

		// page object holds data about pagination and sorting
		// the object is created based on the url parameters "page", "size" and "sort"
		Page<Student> students = studentService.findAll(page);

		// convert students to DTOs
		List<StudentDTO> studentsDTO = new ArrayList<>();
		for (Student s : students) {
			studentsDTO.add(new StudentDTO(s));
		}

		return new ResponseEntity<>(studentsDTO, HttpStatus.OK);
	}

	@GetMapping(value = "/{id}")
	public ResponseEntity<StudentDTO> getStudent(@PathVariable Integer id) {

		Student student = studentService.findOne(id);

		// studen must exist
		if (student == null) {
			return new ResponseEntity<>(HttpStatus.NOT_FOUND);
		}

		return new ResponseEntity<>(new StudentDTO(student), HttpStatus.OK);
	}

	@PostMapping(consumes = "application/json")
	public ResponseEntity<StudentDTO> saveStudent(@RequestBody StudentDTO studentDTO) {

		Student student = new Student();
		student.setIndex(studentDTO.getIndex());
		student.setFirstName(studentDTO.getFirstName());
		student.setLastName(studentDTO.getLastName());

		student = studentService.save(student);
		return new ResponseEntity<>(new StudentDTO(student), HttpStatus.CREATED);
	}

	@PutMapping(consumes = "application/json")
	public ResponseEntity<StudentDTO> updateStudent(@RequestBody StudentDTO studentDTO) {

		// a student must exist
		Student student = studentService.findOne(studentDTO.getId());

		if (student == null) {
			return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
		}

		student.setIndex(studentDTO.getIndex());
		student.setFirstName(studentDTO.getFirstName());
		student.setLastName(studentDTO.getLastName());

		student = studentService.save(student);
		return new ResponseEntity<>(new StudentDTO(student), HttpStatus.OK);
	}

	@DeleteMapping(value = "/{id}")
	public ResponseEntity<Void> deleteStudent(@PathVariable Integer id) {

		Student student = studentService.findOne(id);

		if (student != null) {
			studentService.remove(id);
			return new ResponseEntity<>(HttpStatus.OK);
		} else {
			return new ResponseEntity<>(HttpStatus.NOT_FOUND);
		}
	}

	@GetMapping(value = "/findIndex")
	public ResponseEntity<StudentDTO> getStudentByIndex(@RequestParam String index) {

		Student student = studentService.findByIndex(index);
		if (student == null) {
			return new ResponseEntity<>(HttpStatus.NOT_FOUND);
		}
		return new ResponseEntity<>(new StudentDTO(student), HttpStatus.OK);
	}

	@GetMapping(value = "/findLastName")
	public ResponseEntity<List<StudentDTO>> getStudentsByLastName(@RequestParam String lastName) {

		List<Student> students = studentService.findByLastName(lastName);

		// convert students to DTOs
		List<StudentDTO> studentsDTO = new ArrayList<>();
		for (Student s : students) {
			studentsDTO.add(new StudentDTO(s));
		}
		return new ResponseEntity<>(studentsDTO, HttpStatus.OK);
	}

	@GetMapping(value = "/prezime")
	public ResponseEntity<List<StudentDTO>> pronadjiStudentePoPrezimenu(@RequestParam String lastName) {

		List<Student> students = studentService.pronadjiPoPrezimenu(lastName);

		// convert students to DTOs
		List<StudentDTO> studentsDTO = new ArrayList<>();
		for (Student s : students) {
			studentsDTO.add(new StudentDTO(s));
		}
		return new ResponseEntity<>(studentsDTO, HttpStatus.OK);
	}

	@GetMapping(value = "/findFirstLast")
	public ResponseEntity<List<StudentDTO>> getStudentsByFirstNameAndLastName(@RequestParam String firstName,
			@RequestParam String lastName) {

		List<Student> students = studentService.findByFirstNameAndLastName(firstName, lastName);

		// convert students to DTOs
		List<StudentDTO> studentsDTO = new ArrayList<>();
		for (Student s : students) {
			studentsDTO.add(new StudentDTO(s));
		}
		return new ResponseEntity<>(studentsDTO, HttpStatus.OK);
	}

	@GetMapping(value = "/{studentId}/exams")
	public ResponseEntity<List<ExamDTO>> getStudentExams(@PathVariable Integer studentId) {
		
		//traze se polozeni ispiti studenta, sto znaci da moramo uputiti JOIN FETCH upit
		//kako bismo dobili sve trazene podatke
		Student student = studentService.findOneWithExams(studentId);
		
		//ako je podesen fetchType LAZY i pozovemo findOne umesto findOneWithExams,
		//na poziv getExams bismo dobili LazyInitializationException
		Set<Exam> exams = student.getExams();
		List<ExamDTO> examsDTO = new ArrayList<>();
		for (Exam e : exams) {
			ExamDTO examDTO = new ExamDTO();
			examDTO.setId(e.getId());
			examDTO.setGrade(e.getGrade());
			examDTO.setDate(e.getDate());
			examDTO.setCourse(new CourseDTO(e.getCourse()));
			examDTO.setStudent(new StudentDTO(e.getStudent()));

			examsDTO.add(examDTO);
		}
		return new ResponseEntity<>(examsDTO, HttpStatus.OK);
	}
}
