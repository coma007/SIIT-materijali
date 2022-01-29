package types.country;

import com.opencsv.bean.CsvBindByName;

public class CountrySimple {
	@CsvBindByName(column = "countryName", required = true) // ako ne navedemo eksplicitno naziv kolone, bice koriscen naziv polja
	private String name;
	@CsvBindByName(column = "capitalName", required = true)
	private String capital;

	public CountrySimple() {
	}

	public CountrySimple(String name, String capital) {
		this.name = name;
		this.capital = capital;
	}

	// za pisanje obavezni geteri!
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getCapital() {
		return capital;
	}

	public void setCapital(String capital) {
		this.capital = capital;
	}
	
	
}
