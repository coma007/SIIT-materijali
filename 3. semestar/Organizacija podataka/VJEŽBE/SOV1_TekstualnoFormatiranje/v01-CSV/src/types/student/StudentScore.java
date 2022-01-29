package types.student;

import com.opencsv.bean.CsvBindByPosition;

public class StudentScore {
	
	@CsvBindByPosition(position = 0)
	public String index;
	@CsvBindByPosition(position = 1)
	public String fname;
	@CsvBindByPosition(position = 2)
	public String lname;
	@CsvBindByPosition(position = 3)
	public String subject;
	@CsvBindByPosition(position = 4)
	public int grade;


	
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
	public String getSubject() {
		return subject;
	}
	public void setSubject(String subject) {
		this.subject = subject;
	}
	public int getGrade() {
		return grade;
	}
	public void setGrade(int grade) {
		this.grade = grade;
	}
	@Override
	public String toString() {
		return "StudentScore [index=" + index + ", fname=" + fname + ", lname=" + lname + ", subject=" + subject
				+ ", grade=" + grade + "]";
	}
	
	
	
	

}
