package types.books;

public class Magazine{
	private String Month;
	private int Year;
	private String Title;


	// @JsonProperty("Month")
	public void setMonth(String month) {
		Month = month;
	}
	
	public String getMonth() {
		return Month;
	}
	
	// @JsonProperty("Year")
	public void setYear(int year) {
		Year = year;
	}
	
	public int getYear() {
		return Year;
	}

	public String getTitle() {
		return Title;
	}

	// @JsonProperty("Title")
	public void setTitle(String title) {
		Title = title;
	}

	@Override
	public String toString() {
		return "Magazine [Month=" + Month + ", Year=" + Year + ", Title=" + Title + "]";
	}



	

}
