package p01;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import com.opencsv.CSVReader;

public class CsvReaderBuilder {
	
	static final String CSV_FILE_NAME = "resources/drzave_gradovi.csv";
	static final String DELIMITER = ",";

	public static void main(String[] args) {


		try (CSVReader csv = new CSVReader(new FileReader(CSV_FILE_NAME))){
//			argumenti - to moze samo za klase koje implementiraju autoclosable
			
			String line[] = null;

			while ((line = csv.readNext()) != null) {
				StringBuilder sb = new StringBuilder();
				
				for (int i = 0; i < line.length; i++) {
					sb.append(line[i]);
					
					if (i != line.length) {
						sb.append("$");
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
