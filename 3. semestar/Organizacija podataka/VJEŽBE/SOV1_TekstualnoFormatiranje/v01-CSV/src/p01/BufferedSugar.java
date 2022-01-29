package p01;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class BufferedSugar {

	static final String CSV_FILE_NAME = "resources/drzave_gradovi.csv";
	static final String DELIMITER = ",";

	public static void main(String[] args) {


		try (BufferedReader br = new BufferedReader(new FileReader(CSV_FILE_NAME))){
//			u ovom slucaju ne treba finally da bi se zatvorio buff reader
//			argumenti - to moze samo za klase koje implementiraju autoclosable
			
			String line;

			while ((line = br.readLine()) != null) {
				String tokens[] = line.split(DELIMITER);
				for (String token : tokens) {
					System.out.print(token + "|");
				}
				System.out.println("");
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

