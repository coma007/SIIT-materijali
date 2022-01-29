package z03_2018;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.List;

import com.opencsv.CSVReader;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

import types.student.StudentScore;

public class CSVFaculty {
	
	static String filename = "resources/dodatni_materijali/input3_0.csv";
	
	public static void main(String[] args) {
		
		readHeader();
		readOther();
		
		
	}

	private static void readOther() {

		try (Reader r = new FileReader(filename)) {
			
			CsvToBean<StudentScore> ctb = new CsvToBeanBuilder<StudentScore>(r).withSkipLines(10).withType(StudentScore.class).withSeparator(',').build();
			List<StudentScore> lss = ctb.parse();
			
			for (StudentScore ss : lss) {
				System.out.println(ss);
			}
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

	private static void readHeader() {

		try {
			CSVReader read = new CSVReader(new FileReader(new File(filename)));
			
			int i = 0;
			while (i < 5) {
				
				String[] data = read.readNext();
				for (String s: data) {
					System.out.println(s);
				}
				i++;
				
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
	

}
