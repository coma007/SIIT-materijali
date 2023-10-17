package rs.ac.uns.ftn.wines.service.interfaces;

import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpHeaders;
import rs.ac.uns.ftn.wines.domain.Wine;

import java.util.List;

public interface WineService {

    List<Wine> getAll(Pageable pageable, HttpHeaders hh);

    void add(Wine wine);

}
