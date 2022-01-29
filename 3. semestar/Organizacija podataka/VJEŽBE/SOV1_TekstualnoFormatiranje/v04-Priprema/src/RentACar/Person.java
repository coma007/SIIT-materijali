package RentACar;

import com.opencsv.bean.CsvBindByPosition;

public class Person {

	@CsvBindByPosition(position =  0)
	public String fname;
	@CsvBindByPosition(position =  1)
	public String lname;
	@CsvBindByPosition(position =  2)
	public String jmbg;
	@CsvBindByPosition(position =  3)
	public double total;
	@CsvBindByPosition(position =  4)
	public long avgDays;
	
	
	public Person() {
	}


	public Person(String fname, String lname, String jmbg) {
		this.fname = fname;
		this.lname = lname;
		this.jmbg = jmbg;
	}


	public String getFname() {
		return fname;
	}


	public void setFname(String fname) {
		this.fname = fname;
	}


	public String getLname() {
		return lname;
	}


	public void setLname(String lname) {
		this.lname = lname;
	}


	public String getJmbg() {
		return jmbg;
	}


	public void setJmbg(String jmbg) {
		this.jmbg = jmbg;
	}


	public double getTotal() {
		return total;
	}


	public void setTotal(double total) {
		this.total = total;
	}


	public long getAvgDays() {
		return avgDays;
	}


	public void setAvgDays(long avgDays) {
		this.avgDays = avgDays;
	}


	@Override
	public String toString() {
		return "Person [fname=" + fname + ", lname=" + lname + ", jmbg=" + jmbg + ", total=" + total + ", avgDays="
				+ avgDays + "]";
	}
	
	
	
	
}
