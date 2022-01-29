package types.country;

import com.opencsv.bean.CsvBindByPosition;

public class Country_ColumnPositions {
	@CsvBindByPosition(position = 0, required = true)
	private String countryName;
	@CsvBindByPosition(position = 1, required = true)
	private String capitalName;
	@CsvBindByPosition(position = 2, required = true)
	private String capitalLatitude;
	@CsvBindByPosition(position = 3, required = true)
	private String capitalLongitude;
	@CsvBindByPosition(position = 4, required = true)
	private String countryCode;
	@CsvBindByPosition(position = 5, required = true)
	private String continentName;

	// Obavezno mora imati prazan konstruktor!
	public Country_ColumnPositions() {
	}

	public Country_ColumnPositions(String countryName, String capitalName, String capitalLatitude,
			String capitalLongitude, String countryCode, String continentName) {
		this.countryName = countryName;
		this.capitalName = capitalName;
		this.capitalLatitude = capitalLatitude;
		this.capitalLongitude = capitalLongitude;
		this.countryCode = countryCode;
		this.continentName = continentName;
	}

	public String getCountryName() {
		return countryName;
	}

	public void setCountryName(String countryName) {
		this.countryName = countryName;
	}

	public String getCapitalName() {
		return capitalName;
	}

	public void setCapitalName(String capitalName) {
		this.capitalName = capitalName;
	}

	public String getCapitalLatitude() {
		return capitalLatitude;
	}

	public void setCapitalLatitude(String capitalLatitude) {
		this.capitalLatitude = capitalLatitude;
	}

	public String getCapitalLongitude() {
		return capitalLongitude;
	}

	public void setCapitalLongitude(String capitalLongitude) {
		this.capitalLongitude = capitalLongitude;
	}

	public String getCountryCode() {
		return countryCode;
	}

	public void setCountryCode(String countryCode) {
		this.countryCode = countryCode;
	}

	public String getContinentName() {
		return continentName;
	}

	public void setContinentName(String continentName) {
		this.continentName = continentName;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((capitalLatitude == null) ? 0 : capitalLatitude.hashCode());
		result = prime * result + ((capitalLongitude == null) ? 0 : capitalLongitude.hashCode());
		result = prime * result + ((capitalName == null) ? 0 : capitalName.hashCode());
		result = prime * result + ((continentName == null) ? 0 : continentName.hashCode());
		result = prime * result + ((countryCode == null) ? 0 : countryCode.hashCode());
		result = prime * result + ((countryName == null) ? 0 : countryName.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Country_ColumnPositions other = (Country_ColumnPositions) obj;
		if (capitalLatitude == null) {
			if (other.capitalLatitude != null)
				return false;
		} else if (!capitalLatitude.equals(other.capitalLatitude))
			return false;
		if (capitalLongitude == null) {
			if (other.capitalLongitude != null)
				return false;
		} else if (!capitalLongitude.equals(other.capitalLongitude))
			return false;
		if (capitalName == null) {
			if (other.capitalName != null)
				return false;
		} else if (!capitalName.equals(other.capitalName))
			return false;
		if (continentName == null) {
			if (other.continentName != null)
				return false;
		} else if (!continentName.equals(other.continentName))
			return false;
		if (countryCode == null) {
			if (other.countryCode != null)
				return false;
		} else if (!countryCode.equals(other.countryCode))
			return false;
		if (countryName == null) {
			if (other.countryName != null)
				return false;
		} else if (!countryName.equals(other.countryName))
			return false;
		return true;
	}

	@Override
	public String toString() {
		return "Country [countryName=" + countryName + ", capitalName=" + capitalName + ", capitalLatitude="
				+ capitalLatitude + ", capitalLongitude=" + capitalLongitude + ", countryCode=" + countryCode
				+ ", continentName=" + continentName + "]";
	}

}
