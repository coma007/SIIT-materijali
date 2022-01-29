package p01;

import java.io.File;
import java.io.IOException;
import java.util.Map;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.MapperFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

public class JSONDirect {

	public static void main(String[] args) throws JsonParseException, JsonMappingException, IOException {
		
		ObjectMapper mapper = new ObjectMapper();
		mapper.configure(MapperFeature.ACCEPT_CASE_INSENSITIVE_PROPERTIES, true);
		
		@SuppressWarnings("unchecked")
		Map<String, Object> book = mapper.readValue(new File("resources/Example1_Book.json"), Map.class);
		System.out.println(book);
		
		book.put("newAttribute", "newValue");
		mapper.enable(SerializationFeature.INDENT_OUTPUT);
		mapper.writeValue(new File("resources/Example1_Book_changed.json"), book);
		
	}
}
