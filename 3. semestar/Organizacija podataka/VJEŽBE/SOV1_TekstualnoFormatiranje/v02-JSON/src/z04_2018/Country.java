package z04_2018;

import com.opencsv.bean.CsvBindByPosition;

public class Country {
	
	@CsvBindByPosition(position = 0)
	public String CountryName;
	@CsvBindByPosition(position = 1)
	public String CapitalName;
	@CsvBindByPosition(position = 2)
	public double CapitalLatitude;
	@CsvBindByPosition(position = 3)
	public double CapitalLongitude;
	@CsvBindByPosition(position = 4)
	public String CountryCode;
	@CsvBindByPosition(position = 5)
	public String ContinentName;
	
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
	public double getCapitalLatitude() {
		return CapitalLatitude;
	}
	public void setCapitalLatitude(double capitalLatitude) {
		CapitalLatitude = capitalLatitude;
	}
	public double getCapitalLongitude() {
		return CapitalLongitude;
	}
	public void setCapitalLongitude(double capitalLongitude) {
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
