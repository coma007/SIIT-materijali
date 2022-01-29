package RentACar;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import com.fasterxml.jackson.core.JsonGenerationException;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.opencsv.bean.StatefulBeanToCsv;
import com.opencsv.bean.StatefulBeanToCsvBuilder;
import com.opencsv.exceptions.CsvDataTypeMismatchException;
import com.opencsv.exceptions.CsvRequiredFieldEmptyException;

public class z05AllFilter {

	static String filename = "resources/car/rents.json";
	static String filenameCSV = "resources/car/people.csv";
	static String filenameJSON = "resources/car/sorted.json";
	static String filenameYAML = "resources/car/search.yaml";

	public static void main(String[] args) throws JsonParseException, JsonMappingException, IOException {

		List<Car> rents = parseJSON();
		writeYaml(rents);
		writeCSV(rents);
		writeJSON(rents);

	}

	private static void writeJSON(List<Car> rents) throws JsonGenerationException, JsonMappingException, IOException {
		
		ObjectMapper om = new ObjectMapper();
		Collections.sort(rents, Comparator.reverseOrder());
		om.enable(SerializationFeature.INDENT_OUTPUT);
		om.writeValue(new File(filenameJSON), rents);
		
	}

	private static void writeCSV(List<Car> rents) {

		List<Person> persons = new ArrayList<Person>();
		for (Car c : rents) {
			persons.add(c.getPerson());
		}
		
		try (PrintWriter out = new PrintWriter(new FileWriter(new File(filenameCSV)))) {
			
			StatefulBeanToCsv<Person> btc = new StatefulBeanToCsvBuilder<Person>(out).withApplyQuotesToAll(false).withSeparator(',').build();
			btc.write(persons);
			
		} catch (IOException e) {
			e.printStackTrace();
		} catch (CsvDataTypeMismatchException e) {
			e.printStackTrace();
		} catch (CsvRequiredFieldEmptyException e) {
			e.printStackTrace();
		}
	}

	@SuppressWarnings("deprecation")
	private static void writeYaml(List<Car> rents) {

		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		System.out.println("Mjesec: ");
		int m = sc.nextInt();
		System.out.println("Godina: ");
		int y = sc.nextInt();
		
		List<Car> write = new ArrayList<Car>();
		
		for (Car c: rents) {
			if ((c.getStart().getMonth() == m-1 && c.getStart().getYear() == y-1900) || (c.getEnd().getMonth() == m-1 && c.getEnd().getYear() == y-1900)) {
				write.add(c);
			}
		}
		
		Yaml yaml = new Yaml(new Constructor(Car.class));
		
		try (PrintWriter out = new PrintWriter((new FileWriter(new File(filenameYAML))))) {
			yaml.dump(write, out);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

	private static List<Car> parseJSON() throws JsonParseException, JsonMappingException, IOException {

		List<Car> rents = new ArrayList<Car>();

		ObjectMapper om = new ObjectMapper();
		Car[] cars = om.readValue(new File(filename), Car[].class);
		for (Car c : cars) {
			rents.add(c);
		}

		return rents;

	}
}
