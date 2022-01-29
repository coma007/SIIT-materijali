package p03;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;

import com.opencsv.bean.StatefulBeanToCsv;
import com.opencsv.bean.StatefulBeanToCsvBuilder;
import com.opencsv.exceptions.CsvDataTypeMismatchException;
import com.opencsv.exceptions.CsvRequiredFieldEmptyException;

import types.country.CountrySimple;

public class BeanToCsv {

	static final String out = "resources/drzave_gradovi_beans.csv";

	static final String[] countries = { "Australia, Canberra", "Canada, Ottawa", "China, Bejing", "France, Paris" };

	public static void main(String[] args) {

		List<CountrySimple> content = new ArrayList<CountrySimple>();

		for (String country : countries) {
			content.add(new CountrySimple(country.split(",")[0], country.split(",")[1]));
		}
		
		try (Writer w = new FileWriter(out)) {
			StatefulBeanToCsv<CountrySimple> btc = new StatefulBeanToCsvBuilder<CountrySimple>(w)
					.withApplyQuotesToAll(false).build();
			// kvotuje samo kad mora  
			btc.write(content);
			
		} catch (IOException e) {
			e.printStackTrace();
		} catch (CsvDataTypeMismatchException e) {
			e.printStackTrace();
		} catch (CsvRequiredFieldEmptyException e) {
			e.printStackTrace();
		}

	}
}