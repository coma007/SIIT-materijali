package p02;

import java.io.FileWriter;
import java.io.IOException;

import com.opencsv.CSVWriter;

public class WriterNext {
	
	static final String out = "resources/drzave_gradovi2_next.csv";
	
	static final String header = "Country, City";
	static final String[] countries = {"Australia, Canberra", "Canada, Ottawa", "China, Bejing", "France, Paris"};
	
	public static void main(String[] args) {
		
		try (CSVWriter w = new CSVWriter(new FileWriter(out))) {
			
			w.writeNext(header.split(","));
			for (String country : countries) {
				w.writeNext(country.split(","));
			}
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

}
