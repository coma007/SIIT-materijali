package rs.ac.uns.ftn.wines.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import rs.ac.uns.ftn.wines.domain.WineUser;

import java.util.Optional;

@Repository
public interface UserRepository extends CrudRepository<WineUser, Long> {

    Optional<WineUser> findByUsername(String username);

}
