package rs.ac.uns.ftn.informatika.jpa.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import rs.ac.uns.ftn.informatika.jpa.model.Student;
import rs.ac.uns.ftn.informatika.jpa.repository.StudentRepository;

@Service
public class StudentService {
	
	@Autowired
	private StudentRepository studentRepository;
	
	public Student findOne(Integer id) {
		return studentRepository.findById(id).orElseGet(null);
	}

	public List<Student> findAll() {
		return studentRepository.findAll();
	}
	
	public Page<Student> findAll(Pageable page) {
		return studentRepository.findAll(page);
	}

	public Student save(Student student) {
		return studentRepository.save(student);
	}

	public void remove(Integer id) {
		studentRepository.deleteById(id);
	}
	
	public Student findByIndex(String index) {
		return studentRepository.findOneByIndex(index);
	}
	
	public List<Student> findByLastName(String lastName) {
		return studentRepository.findAllByLastName(lastName);
	}
	
	public List<Student> findByFirstNameAndLastName(String firstName, String lastName) {
		return studentRepository.findByFirstNameAndLastNameAllIgnoringCase(firstName, lastName);
	}
	
	public List<Student> pronadjiPoPrezimenu(String prezime) {
		return studentRepository.pronadjiStudentePoPrezimenu(prezime);
	}
	
	public Student findOneWithExams(Integer studentId) {
		return studentRepository.findOneWithExams(studentId);
	}
}
