package types.country;

import com.opencsv.bean.CsvBindByName;

public class Country {
	@CsvBindByName(column = "CountryName", required = true) // ako ne navedemo eksplicitno naziv kolone, bice koriscen naziv polja
	public String CountryName;
	@CsvBindByName(column = "CapitalName", required = true)
	public String CapitalName;
	@CsvBindByName(column = "CapitalLatitude", required = true)
	public String CapitalLatitude;
	@CsvBindByName(column = "CapitalLongitude", required = true) // ako ne navedemo eksplicitno naziv kolone, bice koriscen naziv polja
	public String CapitalLongitude;
	@CsvBindByName(column = "CountryCode", required = true)
	public String CountryCode;
	@CsvBindByName(column = "ContinentName", required = true) // ako ne navedemo eksplicitno naziv kolone, bice koriscen naziv polja
	public String ContinentName;

	public Country() {
	}

	public Country(String countryName, String capitalName, String capitalLatitude, String capitalLongitude,
			String countryCode, String continentName) {
		CountryName = countryName;
		CapitalName = capitalName;
		CapitalLatitude = capitalLatitude;
		CapitalLongitude = capitalLongitude;
		CountryCode = countryCode;
		ContinentName = continentName;
	}

	public String getCountryName() {
		return CountryName;
	}

	public void setCountryName(String countryName) {
		CountryName = countryName;
	}

	public String getCapitalName() {
		return CapitalName;
	}

	public void setCapitalName(String capitalName) {
		CapitalName = capitalName;
	}

	public String getCapitalLatitude() {
		return CapitalLatitude;
	}

	public void setCapitalLatitude(String capitalLatitude) {
		CapitalLatitude = capitalLatitude;
	}

	public String getCapitalLongitude() {
		return CapitalLongitude;
	}

	public void setCapitalLongitude(String capitalLongitude) {
		CapitalLongitude = capitalLongitude;
	}

	public String getCountryCode() {
		return CountryCode;
	}

	public void setCountryCode(String countryCode) {
		CountryCode = countryCode;
	}

	public String getContinentName() {
		return ContinentName;
	}

	public void setContinentName(String continentName) {
		ContinentName = continentName;
	}

	@Override
	public String toString() {
		return "Country [CountryName=" + CountryName + ", CapitalName=" + CapitalName + ", CapitalLatitude="
				+ CapitalLatitude + ", CapitalLongitude=" + CapitalLongitude + ", CountryCode=" + CountryCode
				+ ", ContinentName=" + ContinentName + "]";
	}

	
	
}
