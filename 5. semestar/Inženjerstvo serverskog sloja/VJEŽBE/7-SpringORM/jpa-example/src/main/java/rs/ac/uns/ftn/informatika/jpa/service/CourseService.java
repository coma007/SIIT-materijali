package rs.ac.uns.ftn.informatika.jpa.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import rs.ac.uns.ftn.informatika.jpa.model.Course;
import rs.ac.uns.ftn.informatika.jpa.repository.CourseRepository;

@Service
public class CourseService {

	@Autowired
	private CourseRepository courseRepository;

	public Course findOne(Integer id) {
		return courseRepository.findById(id).orElseGet(null);
	}

	public List<Course> findAll() {
		return courseRepository.findAll();
	}

	public Page<Course> findAll(Pageable page) {
		return courseRepository.findAll(page);
	}

	public Course save(Course course) {
		return courseRepository.save(course);
	}

	public void remove(Integer id) {
		courseRepository.deleteById(id);
	}
	
	public Course findOneWithExams(Integer courseId) {
		return courseRepository.findOneWithExams(courseId);
	}
}
