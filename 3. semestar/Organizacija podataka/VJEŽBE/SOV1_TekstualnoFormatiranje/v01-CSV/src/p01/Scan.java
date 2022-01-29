package p01;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Scan {

	static final String CSV_FILE_NAME = "resources/drzave_gradovi.csv";
	static final String DELIMITER = ",";

	public static void main(String[] args) {

		Scanner sc = null;

		try {
			sc = new Scanner(new File(CSV_FILE_NAME));
			sc.useDelimiter(DELIMITER);

			while (sc.hasNext()) {
				System.out.print(sc.next() + "|"); 
				// na posljednjem podatku u redu nece procitati "|" vec Enter 
				// i prebacice ga u novi red u ispisu, ali to znaci da u svakom redu sem prvog
				// nije procitao odvojeno posljednji podatak od prvog u narednom redu
			}

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} finally {
			if (sc != null) {
				sc.close();
			}
		}

	}
}
