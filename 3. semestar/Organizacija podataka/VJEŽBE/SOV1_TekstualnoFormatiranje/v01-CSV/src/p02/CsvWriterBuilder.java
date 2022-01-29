package p02;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.opencsv.CSVWriter;
import com.opencsv.CSVWriterBuilder;
import com.opencsv.ICSVWriter;

public class CsvWriterBuilder {
	
	static final String out = "resources/drzave_gradovi2_configured.csv";
	
	static final String header = "Country, City";
	static final String[] countries = {"Australia, Canberra", "Canada, Ottawa", "China, Bejing", "France, Paris"};
	
	public static void main(String[] args) {
		
		List<String[]> content = new ArrayList<String[]>();
		content.add(header.split(","));
		
		for (String country : countries) {
			content.add(country.split(","));
		}
		
		try (CSVWriter w = (CSVWriter) new CSVWriterBuilder(new FileWriter(out))
				.withSeparator('#')
				.withQuoteChar(ICSVWriter.DEFAULT_QUOTE_CHARACTER)
				.withEscapeChar(ICSVWriter.DEFAULT_ESCAPE_CHARACTER)
				.withLineEnd(ICSVWriter.DEFAULT_LINE_END) // nije isto na svim OS...
				.build()) {
			
			// Postoji i stariji nacin bez builder patterna ...
			
			w.writeAll(content);
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

}
