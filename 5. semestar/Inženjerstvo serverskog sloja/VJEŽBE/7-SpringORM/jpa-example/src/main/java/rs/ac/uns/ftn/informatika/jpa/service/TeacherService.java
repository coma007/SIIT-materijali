package rs.ac.uns.ftn.informatika.jpa.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import rs.ac.uns.ftn.informatika.jpa.model.Teacher;
import rs.ac.uns.ftn.informatika.jpa.repository.TeacherRepository;

@Service
public class TeacherService {
	
	@Autowired
	private TeacherRepository teacherRepository;
	
	public Teacher findOne(Integer id) {
		return teacherRepository.findById(id).orElseGet(null);
	}

	public List<Teacher> findAll() {
		return teacherRepository.findAll();
	}
	
	public Page<Teacher> findAll(Pageable page) {
		return teacherRepository.findAll(page);
	}

	public Teacher save(Teacher teacher) {
		return teacherRepository.save(teacher);
	}

	public void remove(Integer id) {
		teacherRepository.deleteById(id);
	}
	
	public List<Teacher> findAllDeleted() {
		return teacherRepository.findAllOnlyDeleted();
	}
	
	public List<Teacher> findAllIncludingDeleted() {
		return teacherRepository.findAllIncludingDeleted();
	}
	
	public Teacher findOneWithCourses(Integer teacherId) {
		return teacherRepository.findOneWithCourses(teacherId);
	}
}
