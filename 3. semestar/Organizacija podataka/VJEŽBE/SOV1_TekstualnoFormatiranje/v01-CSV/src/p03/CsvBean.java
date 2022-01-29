package p03;

import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

import types.country.Country_ColumnNames;
import types.country.Country_ColumnPositions;

public class CsvBean {

	static final String file = "resources/drzave_gradovi.csv";
		
		static final String header = "Country, City";
		static final String[] countries = {"Australia, Canberra", "Canada, Ottawa", "China, Bejing", "France, Paris"};
		
		public static void main(String[] args) {
			
			List<String[]> content = new ArrayList<String[]>();
			content.add(header.split(","));
			
			for (String country : countries) {
				content.add(country.split(","));
			}
			
			try (Reader r = new FileReader(file)) {
				
				CsvToBean<Country_ColumnNames> cn = new CsvToBeanBuilder<Country_ColumnNames>(r)
						.withType(Country_ColumnNames.class).withSeparator(',').build();
				// ne preskace prvu liniju jer je to header, obavezna polja koja mora da procita !
				List<Country_ColumnNames> countryN = cn.parse();
				
				for (Country_ColumnNames c : countryN) {
					System.out.println(c);
				}
				
				System.out.println("#########################");
				
				
			} catch (IOException e) {
				e.printStackTrace();
			}
			
			try (Reader r = new FileReader(file)) {
				
				CsvToBean<Country_ColumnPositions> cp = new CsvToBeanBuilder<Country_ColumnPositions>(r)
						.withType(Country_ColumnPositions.class).withSkipLines(1).withSeparator(',').build();
				// OVDJE PRESKACE HEADER jer mu nisu vazna imena kolona, vec POZICIJE !!!
				List<Country_ColumnPositions> countryP = cp.parse();
				
				for (Country_ColumnPositions c : countryP) {
					System.out.println(c);
				}
				
			} catch (IOException e) {
				e.printStackTrace();
			}
			
		}
	
	

}
