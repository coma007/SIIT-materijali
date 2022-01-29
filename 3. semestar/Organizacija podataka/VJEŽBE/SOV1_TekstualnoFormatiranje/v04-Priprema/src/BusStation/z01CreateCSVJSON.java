package BusStation;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Reader;
import java.io.Writer;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;
import com.opencsv.bean.StatefulBeanToCsv;
import com.opencsv.bean.StatefulBeanToCsvBuilder;
import com.opencsv.exceptions.CsvDataTypeMismatchException;
import com.opencsv.exceptions.CsvRequiredFieldEmptyException;

public class z01CreateCSVJSON {

	static String filenameCSV = "resources/bus/bus.csv";
	static String filenameJSON = "resources/bus/bus.json";

	public static void main(String[] args) throws ParseException {

		List<BusStart> bs = generateBus();
		writeCSV(bs);
		writeJSON();

	}

	private static void writeJSON() {
		
		List<BusStart> bs = new ArrayList<BusStart>();
		
		try (Reader in = new FileReader(new File(filenameCSV))) {
			CsvToBean<BusStart> ctb = new CsvToBeanBuilder<BusStart>(in).withType(BusStart.class).withSkipLines(0).withSeparator(',').build();
			bs = ctb.parse();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		ObjectMapper om = new ObjectMapper();
		
		try (Writer out = new FileWriter(new File(filenameJSON))) {
			om.enable(SerializationFeature.INDENT_OUTPUT);
			
			om.writeValue(out, bs);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

	private static void writeCSV(List<BusStart> bs) {

		try (Writer out = new FileWriter(new File(filenameCSV))) {
			StatefulBeanToCsv<BusStart> btc = new StatefulBeanToCsvBuilder<BusStart>(out).withApplyQuotesToAll(false).withSeparator(',').build();
			btc.write(bs);
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (CsvDataTypeMismatchException e) {
			e.printStackTrace();
		} catch (CsvRequiredFieldEmptyException e) {
			e.printStackTrace();
		}

	}

	private static List<BusStart> generateBus() throws ParseException {
		
		SimpleDateFormat sdfD = new SimpleDateFormat("dd.MM.yyyy.");
		SimpleDateFormat sdfH = new SimpleDateFormat("hh:mm");
		List<BusStart> bs = new ArrayList<BusStart>();
		bs.add(new BusStart("11", "Novi Sad", "Gradiska", sdfD.parse("12.12.2020."), sdfH.parse("12:00"), sdfH.parse("17:00"), 1, 1030, 10));
		bs.add(new BusStart("11", "Gradiska", "Novi Sad", sdfD.parse("12.12.2020."), sdfH.parse("18:00"), sdfH.parse("00:00"), 3, 1030, 10));
		bs.add(new BusStart("11", "Gradiska", "Novi Sad", sdfD.parse("13.12.2020."), sdfH.parse("17:00"), sdfH.parse("23:00"), 3, 1030, 23));
		bs.add(new BusStart("11", "Novi Sad", "Gradiska", sdfD.parse("13.12.2020."), sdfH.parse("15:00"), sdfH.parse("22:00"), 2, 1030, 23));
		bs.add(new BusStart("11", "Novi Sad", "Gradiska", sdfD.parse("14.12.2020."), sdfH.parse("12:00"), sdfH.parse("17:00"), 1, 1030, 11));
		bs.add(new BusStart("11", "Gradiska", "Novi Sad", sdfD.parse("14.12.2020."), sdfH.parse("18:00"), sdfH.parse("00:00"), 3, 1030, 22));
		bs.add(new BusStart("12", "Novi Sad", "Beograd", sdfD.parse("14.12.2020."), sdfH.parse("12:00"), sdfH.parse("14:30"), 5, 300, 52));
		bs.add(new BusStart("12", "Novi Sad", "Beograd", sdfD.parse("14.12.2020."), sdfH.parse("13:00"), sdfH.parse("14:10"), 6, 300, 52));
		bs.add(new BusStart("13", "Novi Sad", "Beograd", sdfD.parse("14.12.2020."), sdfH.parse("14:00"), sdfH.parse("15:10"), 7, 400, 12));
		bs.add(new BusStart("14", "Novi Sad", "Segedin", sdfD.parse("15.12.2020."), sdfH.parse("17:00"), sdfH.parse("11:10"), 3, 1800, 30));
		bs.add(new BusStart("14", "Novi Sad", "Segedin", sdfD.parse("15.12.2020."), sdfH.parse("00:00"), sdfH.parse("04:00"), 3, 1800, 50));
		bs.add(new BusStart("14", "Novi Sad", "Segedin", sdfD.parse("16.12.2020."), sdfH.parse("01:00"), sdfH.parse("05:10"), 3, 1800, 10));
		bs.add(new BusStart("14", "Novi Sad", "Segedin", sdfD.parse("17.12.2020."), sdfH.parse("00:00"), sdfH.parse("04:00"), 3, 1800, 40));
		return bs;
	}

}
