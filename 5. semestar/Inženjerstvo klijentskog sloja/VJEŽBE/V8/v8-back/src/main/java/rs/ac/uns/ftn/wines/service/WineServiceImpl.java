package rs.ac.uns.ftn.wines.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpHeaders;
import org.springframework.stereotype.Service;
import rs.ac.uns.ftn.wines.domain.Wine;
import rs.ac.uns.ftn.wines.repository.WineRepository;
import rs.ac.uns.ftn.wines.service.interfaces.WineService;

import java.util.List;
import java.util.Optional;

@Service
public class WineServiceImpl implements WineService {

    private WineRepository wineRepository;

    @Autowired
    public WineServiceImpl(WineRepository wineRepository) {
        this.wineRepository = wineRepository;
    }

    @Override
    public List<Wine> getAll() {
        return (List<Wine>) this.wineRepository.findAll();
    }

    @Override
    public Optional<Wine> getWine(String id) {
        return  this.wineRepository.findById(Long.parseLong(id));
    }

    public void add(Wine wine) {
        this.wineRepository.save(wine);
    }

}
