package rs.ac.uns.ftn.wines.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.stereotype.Service;
import rs.ac.uns.ftn.wines.domain.WineUser;
import rs.ac.uns.ftn.wines.exceptions.NotFoundException;
import rs.ac.uns.ftn.wines.repository.UserRepository;
import rs.ac.uns.ftn.wines.security.UserFactory;

@Service
public class UserDetailsServiceImpl implements UserDetailsService {

    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) {
        WineUser wineUser = this.userRepository.findByUsername(username)
                .orElseThrow(() -> new NotFoundException(String.format("User with username '%s' is not found!", username)));

        return UserFactory.create(wineUser);
    }


}
