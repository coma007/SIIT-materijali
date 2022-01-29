package p01;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import com.opencsv.CSVParser;
import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;

public class CsvParserBuilder {
	
	static final String CSV_FILE_NAME = "resources/indijska_hrana.csv";
	static final String DELIMITER = ",";

	public static void main(String[] args) {

		CSVParser p = new CSVParserBuilder().withSeparator(';').withQuoteChar('\'').build();

		try (CSVReader r = new CSVReaderBuilder(new FileReader(CSV_FILE_NAME)).withCSVParser(p)
				.withSkipLines(1).build()) {
//			argumenti - to moze samo za klase koje implementiraju autoclosable
			
			String[] row = null;
			
			while ((row = r.readNext()) != null) {
				StringBuilder sb = new StringBuilder();
				
				for (int i = 0; i < row.length; i++) {
					sb.append(row[i]);
					
					if (i != row.length) {
						sb.append("|");
					}
				}
				System.out.println(sb);
			}
		} 
		catch (FileNotFoundException e1) {
			e1.printStackTrace();
		} 
		catch (IOException e) {
			e.printStackTrace();
		} 
		
	}

}
