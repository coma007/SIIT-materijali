package z02;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

import com.fasterxml.jackson.core.JsonEncoding;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonParseException;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

import types.country.Country;

public class JSONCountries {

	static String filenameCSV = "resources/countries_cities.csv";

	static String EuropeFile = "resources/europe.json";
	static String AsiaFile = "resources/asia.json";
	static String AfricaFile = "resources/africa.json";
	static String NAmericaFile = "resources/namerica.json";
	static String SAmericaFile = "resources/samerica.json";
	static String AustraliaFile = "resources/australia.json";
	static String AntarticaFile = "resources/antartica.json";

	static String[] array = { EuropeFile, AsiaFile, AfricaFile, NAmericaFile, SAmericaFile, AustraliaFile,
			AntarticaFile };
	static List<Country> Europe = new ArrayList<Country>();
	static List<Country> Asia = new ArrayList<Country>();
	static List<Country> NAmerica = new ArrayList<Country>();
	static List<Country> Africa = new ArrayList<Country>();
	static List<Country> SAmerica = new ArrayList<Country>();
	static List<Country> Australia = new ArrayList<Country>();
	static List<Country> Antartica = new ArrayList<Country>();
	static List<List<Country>> continents = new ArrayList<List<Country>>();

	static List<Country> all = new ArrayList<Country>();

	public static void main(String[] args) throws JsonParseException, IOException {

		continents.add(Europe);
		continents.add(Asia);
		continents.add(Africa);
		continents.add(NAmerica);
		continents.add(SAmerica);
		continents.add(Australia);
		continents.add(Antartica);

		readContinents();
		writeContinents();

	}

	private static void writeContinents() throws JsonParseException, IOException {

		for (int i = 0; i < array.length; i++) {
			writeCountries(array[i], continents.get(i));
		}

	}

	private static void writeCountries(String string, List<Country> list) throws JsonParseException, IOException {

		JsonFactory jf = new JsonFactory();
		JsonGenerator jg = jf.createGenerator(new File(string), JsonEncoding.UTF8).useDefaultPrettyPrinter();

		for (Country c : list) {
			jg.writeStartObject();
			jg.writeStringField("CountryName", c.CountryName);
			jg.writeStringField("CapitalName", c.CapitalName);
			jg.writeStringField("CapitalLatitude", c.CapitalLatitude);
			jg.writeStringField("CapitalLongitude", c.CapitalLongitude);
			jg.writeStringField("CountryCode", c.CountryCode);
			jg.writeStringField("ContinentName", c.ContinentName);
			jg.writeEndObject();
		}

		jg.close();
	}

	private static void readContinents() {

		try (Reader r = new FileReader(filenameCSV)) {
			CsvToBean<Country> bean = new CsvToBeanBuilder<Country>(r).withType(Country.class).withSeparator(',')
					.build();
			all = bean.parse();

			for (Country c : all) {
				set(c);
			}

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static void set(Country c) {

		switch (c.getContinentName()) {

		case ("Europe"):
			Europe.add(c);
			break;
		case ("Asia"):
			Asia.add(c);
			break;
		case ("Africa"):
			Africa.add(c);
			break;
		case ("NAmerica"):
			NAmerica.add(c);
			break;
		case ("SAmerica"):
			SAmerica.add(c);
			break;
		case ("Australia"):
			Australia.add(c);
			break;
		default:
			Antartica.add(c);
		}

	}

}
