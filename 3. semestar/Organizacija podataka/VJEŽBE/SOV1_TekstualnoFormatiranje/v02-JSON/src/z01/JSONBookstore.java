package z01;

import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.MapperFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

import types.books.Bookstore;

public class JSONBookstore {
	
	static String filename = "resources/Bookstore.json";
	
	public static void main(String[] args) throws JsonProcessingException, IOException {
		
		ObjectMapper mp = new ObjectMapper();
		mp.configure(MapperFeature.ACCEPT_CASE_INSENSITIVE_PROPERTIES, true);
		Bookstore bs = new Bookstore();
		
		bs = mp.readValue(new File(filename), Bookstore.class);
		System.out.println(bs);
	}

}
