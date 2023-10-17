package rs.ac.uns.ftn.wines.security;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.AuthorityUtils;
import rs.ac.uns.ftn.wines.domain.WineUser;

import java.util.Collection;

public class UserFactory {

    public static SecurityUser create(WineUser wineUser) {
        Collection<? extends GrantedAuthority> authorities;
        try {
            authorities = AuthorityUtils.commaSeparatedStringToAuthorityList(wineUser.getAuthorities());
        } catch (Exception e) {
            authorities = null;
        }

        return new SecurityUser(
            wineUser.getId(),
            wineUser.getUsername(),
            wineUser.getPassword(),
            authorities
        );
    }


}
