package rs.ac.uns.ftn.informatika.jpa.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;

import rs.ac.uns.ftn.informatika.jpa.model.Teacher;

public interface TeacherRepository extends JpaRepository<Teacher, Integer> {
	
	@Query("select t from Teacher t join fetch t.courses e where t.id =?1")
	public Teacher findOneWithCourses(Integer teacherId);

	//-------Primeri baratanja sa Hibernate soft delete - logickim brisanjem
	@Query(value = "UPDATE Teacher t SET t.deleted = false WHERE t.id = ?1")
	@Modifying
	public void restoreById(Long id);

	//mora biti native query a ne JPQL da bi se izbeglo da Hibernate doda WHERE klauzulu sa deleted = false
	@Query(value = "SELECT id, first_name, last_name, deleted FROM teacher", nativeQuery = true)
	public List<Teacher> findAllIncludingDeleted();

	//mora biti native query a ne JPQL da bi se izbeglo da Hibernate doda WHERE klauzulu sa deleted = false
	@Query(value = "SELECT id, first_name, last_name, deleted FROM teacher AS t WHERE t.deleted = true", nativeQuery = true)
	public List<Teacher> findAllOnlyDeleted();
}
