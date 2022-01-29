package z04_2018;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

public class JSONCountries {
	
	static String filename = "src/z04_2018/countries_cities.csv";
	static String filenameNew = "src/z04_2018/countries_cities.json";
	
	public static void main(String[] args) {
		
		List<Country> countries = readCSV();
		
		List<Country> Europe = new ArrayList<Country>();
		List<Country> Asia = new ArrayList<Country>();
		List<Country> Africa = new ArrayList<Country>();
		List<Country> NAmerica = new ArrayList<Country>();
		List<Country> SAmerica = new ArrayList<Country>();
		List<Country> Australia = new ArrayList<Country>();
		List<Country> Antartica = new ArrayList<Country>();
		
		for (Country c: countries) {
			switch(c.getContinentName()) {
			case "Europe":
				Europe.add(c);
				break;
			case "Asia":
				Asia.add(c);
				break;
			case "Africa":
				Africa.add(c);
				break;
			case "North America":
				NAmerica.add(c);
				break;
			case "South America":
				SAmerica.add(c);
				break;
			case "Australia":
				Australia.add(c);
				break;
			case "Antartica":
				Antartica.add(c);
				break;
			}
		}
		
		Map<String, Country> north = new HashMap<String, Country>();
		
		north.put("Europe", getNorth(Europe));
		north.put("Asia", getNorth(Asia));
		north.put("Africa", getNorth(Africa));
		north.put("NAmerica", getNorth(NAmerica));
		north.put("SAmerica", getNorth(SAmerica));
		north.put("Australia", getNorth(Australia));
		north.put("Antartica", getNorth(Antartica));
		
		createJSON(north);
		
	}

	private static void createJSON(Map<String, Country> north) {

		ObjectMapper om = new ObjectMapper();
		try {
			om.writeValue(new File(filenameNew), north);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

	private static Country getNorth(List<Country> continent) {
		
		double northest = - 100;
		Country north = null;
		for (Country c: continent) {
			if (c.getCapitalLongitude() > northest) {
				north = c;
				northest = c.getCapitalLongitude();
			}
		}
		return north;
	}

	private static List<Country> readCSV() {
		
		List<Country> countries = new ArrayList<Country>();
		
		try (Reader r = new FileReader(new File(filename))) {
			
			CsvToBean<Country> ctb = new CsvToBeanBuilder<Country>(r).withType(Country.class).withQuoteChar('\"').withSkipLines(1).build();
			countries = ctb.parse(); 
			
			for (Country c: countries) {
				System.out.println(c);
			}
					
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return countries;
	}

}
