package rs.ac.uns.ftn.informatika.jpa.repository;

import java.io.Serializable;

import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.NoRepositoryBean;
import org.springframework.data.repository.Repository;

/*
 * Nacin za pisanje custom baznog repozitorijuma umesto koriscenja predefinisanih Spring Data JPA repozitorijuma:
 * 1. Kreira se interfejs koji nasledjuje Repository ili je anotiran sa @Repository
 * 2. Dodaju se metode po izboru ali se mora voditi racuna da njihov potpis odgovara
 * potpisima metoda osnovnih Spring Data interfejsa
 * 3. Koristi se novi interfejs kao bazni za sve custom repozitorijume koji se dalje pisu
 * 4. Koristi se @NoRepositoryBean anotacija kako Spring Data repository infrastruktura
 * ne bi pokusala da napravi bean instance.
 */
@NoRepositoryBean
public interface CustomRepository<T, ID extends Serializable> extends Repository<T, ID> {

	Iterable<T> findAll(Pageable sort);

	<S extends T> S save(S entity);
}
