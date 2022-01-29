package types.books;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Bookstore {
	
	private List<Book> Books;
	private List<Magazine> Magazines;
	public List<Book> getBooks() {
		return Books;
	}
	
	 @JsonProperty("Books")
	public void setBooks(List<Book> books) {
		this.Books = books;
	}
	 

	 @JsonProperty("Magazines")
	public List<Magazine> getMagazines() {
		return Magazines;
	}
	public void setMagazines(List<Magazine> magazines) {
		this.Magazines = magazines;
	}
	@Override
	public String toString() {
		return "Bookstore [books=" + Books + ", magazines=" + Magazines + "]";
	}
	
	

}
