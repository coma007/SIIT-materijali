package types.books;


public class AuthorBook {
	
	public String fname;
	public String lname;
	public String btitle;
	
	
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
	public String getBtitle() {
		return btitle;
	}
	public void setBtitle(String btitle) {
		this.btitle = btitle;
	}
	@Override
	public String toString() {
		return "AuthorBook [fname=" + fname + ", lname=" + lname + ", btitle=" + btitle + "]";
	}
	
	

}
