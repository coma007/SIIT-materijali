package p03;

import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import types.books.AuthorBook;

public class JSONTree {
	
	static String filenameMap = "resources/Example2_Book.json";
	static String filenameCh = "resources/Book_changed.json";
	
	public static void main(String[] args) throws JsonProcessingException, IOException {
		
		ObjectMapper mp = new ObjectMapper();
		AuthorBook ab = new AuthorBook();
		
		JsonNode root = mp.readTree(new File(filenameMap));
		ab.setBtitle(root.path("Title").textValue());
		
		ab.setLname(root.at("/Author/Last Name").textValue());
		JsonNode node = root.path("Author");
		ab.setFname(node.path("First Name").textValue());
		
		System.out.println(ab);
	}

}
