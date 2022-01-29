package p02;

import java.util.List;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

import com.opencsv.CSVWriter;

public class WriterAll {
	
	static final String out = "resources/drzave_gradovi2_all.csv";
	
	static final String header = "Country, City";
	static final String[] countries = {"Australia, Canberra", "Canada, Ottawa", "China, Bejing", "France, Paris"};
	
	public static void main(String[] args) {
		
		List<String[]> content = new ArrayList<String[]>();
		content.add(header.split(","));
		
		for (String country : countries) {
			content.add(country.split(","));
		}
		
		try (CSVWriter w = new CSVWriter(new FileWriter(out))) {
			
			w.writeAll(content);
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

}
