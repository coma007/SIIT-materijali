package z01;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Reader;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;
import com.opencsv.bean.StatefulBeanToCsv;
import com.opencsv.bean.StatefulBeanToCsvBuilder;
import com.opencsv.exceptions.CsvDataTypeMismatchException;
import com.opencsv.exceptions.CsvRequiredFieldEmptyException;

import types.point.Point;

public class CSVPoints {
	
	static public String filename = "resources/points.csv";
	static public String filenameR = "resources/pointsR.csv";
	static public String filenameSort = "resources/pointsSort.csv";
	
	public static void main(String[] args) {
		
		List<Point> points = read();
		
		writeAll(points, filenameR);
		
		Collections.sort(points, Collections.reverseOrder());
		writeAll(points, filenameSort);
		
	}
	
	static void writeAll(List<Point> pts, String file) {
		
		try (Writer writer = new FileWriter(new File(file))) {
			
			StatefulBeanToCsv<Point> btc = new StatefulBeanToCsvBuilder<Point>(writer).withApplyQuotesToAll(false).withSeparator('#').build();
			btc.write(pts);
			
		} catch (IOException e) {
			e.printStackTrace();
		} catch (CsvDataTypeMismatchException e) {
			e.printStackTrace();
		} catch (CsvRequiredFieldEmptyException e) {
			e.printStackTrace();
		}
		
		
	}
	


	static List<Point> read() {

		List<Point> ps = new ArrayList<Point>();
		try (Reader reader = new FileReader(filename)) {
			CsvToBean<Point> ctb = new CsvToBeanBuilder<Point>(reader).withSkipLines(1).withType(Point.class).withSeparator(',').build();			
			ps = ctb.parse();
			for (Point p : ps) {
				p.countDistance();
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return ps;

	}
}
