package rs.ac.uns.ftn.wines.repository;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import rs.ac.uns.ftn.wines.domain.Wine;

@Repository
public interface WineRepository extends CrudRepository<Wine, Long> {

    Page<Wine> findAll(Pageable page);
}
