package rs.ac.uns.ftn.wines.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.support.PagedListHolder;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
import rs.ac.uns.ftn.wines.domain.Wine;
import rs.ac.uns.ftn.wines.service.interfaces.WineService;

import java.util.List;

@RestController
public class WineController {

    private WineService wineService;

    @Autowired
    public WineController(WineService wineService) {
        this.wineService = wineService;
    }

    @PreAuthorize("hasAnyAuthority('WINE_USER, ADMIN')")
    @GetMapping(
            value = "/getAll",
            produces = MediaType.APPLICATION_JSON_VALUE
    )
    public ResponseEntity getAll(Pageable page) {

        HttpHeaders header = new HttpHeaders();
        List<Wine> holder = this.wineService.getAll(page, header);

        return new ResponseEntity<>(holder, header, HttpStatus.OK);
    }

    @PreAuthorize("hasAnyAuthority('WINE_USER, ADMIN')")
    @PostMapping(
            value = "/add",
            produces = MediaType.APPLICATION_JSON_VALUE
    )
    public ResponseEntity add(@RequestBody Wine wine) {

        this.wineService.add(wine);

        return new ResponseEntity<>("Successful add!", HttpStatus.OK);
    }

}
