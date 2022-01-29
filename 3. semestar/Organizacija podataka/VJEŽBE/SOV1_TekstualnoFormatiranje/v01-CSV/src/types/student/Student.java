package types.student;


public class Student {
	
	public String index;
	public String fname;
	public String lname;
	
	public String getIndex() {
		return index;
	}
	public void setIndex(String index) {
		this.index = index;
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
	
	@Override
	public String toString() {
		return "Student [index=" + index + ", fname=" + fname + ", lname=" + lname + "]";
	}
	
	

}
