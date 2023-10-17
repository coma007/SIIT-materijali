package rs.ac.uns.ftn.wines.service.interfaces;

import rs.ac.uns.ftn.wines.domain.Wine;

import java.util.List;
import java.util.Optional;

public interface WineService {

    List<Wine> getAll();

    Optional<Wine> getWine(String id);

    void add(Wine wine);

}
