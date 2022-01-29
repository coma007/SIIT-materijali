package types.invoice;

public class Address {
	
	public String lines;
	public String city;
	public String state;
	public String postal;
	public String getLines() {
		return lines;
	}
	public void setLines(String lines) {
		this.lines = lines;
	}
	public String getCity() {
		return city;
	}
	public void setCity(String city) {
		this.city = city;
	}
	public String getState() {
		return state;
	}
	public void setState(String state) {
		this.state = state;
	}
	public String getPostal() {
		return postal;
	}
	public void setPostal(String postal) {
		this.postal = postal;
	}
	@Override
	public String toString() {
		return "Address [lines=" + lines + ", city=" + city + ", state=" + state + ", postal=" + postal + "]";
	}
	
	

}
