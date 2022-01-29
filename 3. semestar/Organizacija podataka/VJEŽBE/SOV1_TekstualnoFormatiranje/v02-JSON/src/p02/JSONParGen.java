package p02;

import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.core.JsonEncoding;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonToken;

import types.books.AuthorBook;

public class JSONParGen {

	static String filename = "resources/Example2_Book_generated.json";

	public static void main(String[] args) throws IOException {

		generateJSON();

		AuthorBook ab = new AuthorBook();
		parseJSON(ab);
		System.out.println(ab);

	}

	private static void parseJSON(AuthorBook ab) throws JsonParseException, IOException {

		JsonFactory jf = new JsonFactory();
		JsonParser jp = jf.createParser(new File(filename));

		jp.nextToken();

		while (jp.nextToken() != JsonToken.END_OBJECT) {
			String fieldName = jp.getCurrentName();
			jp.nextToken();

			if ("Author".equals(fieldName)) {

				while (jp.nextToken() != JsonToken.END_OBJECT) {
					String nameField = jp.getCurrentName();
					jp.nextToken();
					
					if (("First Name").equals(nameField)) {
						ab.setFname(jp.getText());
					}
					else if (("Last Name").equals(nameField)){
						ab.setLname(jp.getText());
					}
				}
			}
			else if ("Title".equals(fieldName)) {
				ab.setBtitle(jp.getText());
			}
		}
		jp.close();
	}

	public static void generateJSON() throws IOException {

		JsonFactory jf = new JsonFactory();
		JsonGenerator jg = jf.createGenerator(new File(filename), JsonEncoding.UTF8).useDefaultPrettyPrinter();

		jg.writeStartObject();
		jg.writeObjectFieldStart("Author");
		jg.writeStringField("First Name", "Jovan");
		jg.writeStringField("Last Name", "Dučić");
		jg.writeEndObject();

		jg.writeStringField("Title", "Blago cara Radovana");
		jg.writeEndObject();

		jg.close();
	}
}
