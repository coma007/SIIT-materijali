package types.books;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;

@JsonAutoDetect(fieldVisibility = Visibility.ANY)
public class Author {
	private String First_Name;
	private String Last_Name;

	@Override
	public String toString() {
		return "Author {First_Name=" + First_Name + ", Last_Name=" + Last_Name + "}";
	}

}
