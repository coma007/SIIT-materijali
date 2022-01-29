package Cinema;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.text.Format;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;

import com.fasterxml.jackson.core.JsonGenerationException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.opencsv.bean.StatefulBeanToCsv;
import com.opencsv.bean.StatefulBeanToCsvBuilder;
import com.opencsv.exceptions.CsvDataTypeMismatchException;
import com.opencsv.exceptions.CsvRequiredFieldEmptyException;

public class zpCreateCSV {

	static String filenameCSV = "resources/cinema/projections.csv";
	static String filenameJSONMovie = "resources/cinema/movies.json";
	static String filenameJSONRoom = "resources/cinema/rooms.json";
	static String fileYAML = "resources/cinema/filters.yaml";

	public static void main(String[] args) {

		List<MovieProjection> mp = writeCSV();
		Object[] data = writeJSONs(mp);
		HashMap<String, Room> rooms = (HashMap<String, Room>) data[0];
		HashMap<String, Movie> movies = (HashMap<String, Movie>) data[1];
		
		Movie maxM = findMaxMovie(movies.values());
		Room maxR = findMaxRoom(rooms.values());
		Room moneyR = findMoneyRoom(mp, rooms);
		
		HashMap<String, Object> filter = new HashMap<String, Object>();
		filter.put("Najduzi film", maxM);
		filter.put("Najveca sala", maxR);
		filter.put("Najprofitabilnija sala", moneyR);
		
		writeYAML(filter);

	}

	private static void writeYAML(HashMap<String, Object> filter) {

		DumperOptions doo = new DumperOptions();
		doo.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
		Yaml y = new Yaml(doo);
		try (Writer out = new FileWriter(new File(fileYAML))) {
			y.dump(filter, out);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

	private static Room findMoneyRoom(List<MovieProjection> mp, HashMap<String, Room> rooms) {

		HashMap<Room, Double> rm = new HashMap<Room, Double>();
		for (MovieProjection proj : mp) {
			if (rm.get(rooms.get(proj.getRoomId())) == null) {
				rm.put(rooms.get(proj.getRoomId()), proj.getPrice());
			}
			else {
				rm.put(rooms.get(proj.getRoomId()), rm.get(rooms.get(proj.getRoomId())) + proj.getPrice());
			}
		}
		
		Room maxi = null;
		double money = 0;
		for (Room r : rm.keySet()) {
			if (rm.get(r) > money) {
				money = rm.get(r);
				maxi = r;
			}
		}
		
		return maxi;
	}

	private static Room findMaxRoom(Collection<Room> values) {
		Room maxi = null;
		int cap = 0;
		for (Room r : values) {
			if (cap < r.getRoomCapacity())  {
				cap = r.getRoomCapacity();
				maxi = r;
			}
				
		}		
		return maxi;
	}


	private static Movie findMaxMovie(Collection<Movie> values) {
		Movie maxi = null;
		int time = 0;
		for (Movie m: values) {
			if (time < m.getLength())  {
				time = m.getLength();
				maxi = m;
			}
				
		}		
		return maxi;
	
	}

	private static Object[] writeJSONs(List<MovieProjection> mp) {
		Object[] rv = new Object[2];
		HashMap<String, Room> rs = new HashMap<String, Room>();
		HashMap<String, Movie> ms = new HashMap<String, Movie>();
		for (MovieProjection m : mp) {
			if (ms.get(m.getId()) == null) {
				ms.put(m.getId(), new Movie(m.getId(), m.getMovie(), m.getLength()));
			}
			if (rs.get(m.getRoomId()) == null) {
				rs.put(m.getRoomId(), new Room(m.getRoomId(), m.getRoomName(), m.getRoomCapacity()));
			}
		}
		
		rv[0] = rs;
		rv[1] = ms;

		ObjectMapper om = new ObjectMapper();
		om.enable(SerializationFeature.INDENT_OUTPUT);

		try {
			om.writeValue(new File(filenameJSONMovie), ms);
			om.writeValue(new File(filenameJSONRoom), rs);
		} catch (JsonGenerationException e) {
			e.printStackTrace();
		} catch (JsonMappingException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return rv;
	}

	private static List<MovieProjection> writeCSV() {

		List<MovieProjection> mp = new ArrayList<MovieProjection>();

		Movie m1 = new Movie("11", "Vratice se rode", 120);
		Movie m2 = new Movie("13", "Tri karte za Holivud", 100);
		Movie m3 = new Movie("15", "Crna macka beli macor", 90);
		Room r1 = new Room("112", "Huawei", 200);
		Room r2 = new Room("222", "Room1", 200);
		Room r3 = new Room("332", "Room2", 200);

		mp.add(new MovieProjection(m1, r1, 300));
		mp.add(new MovieProjection(m2, r2, 300));
		mp.add(new MovieProjection(m3, r3, 200));
		mp.add(new MovieProjection(m1, r1, 500));
		mp.add(new MovieProjection(m1, r1, 120));
		mp.add(new MovieProjection(m2, r3, 500));
		mp.add(new MovieProjection(m2, r2, 100));
		mp.add(new MovieProjection(m3, r3, 200));

		try (Writer in = new FileWriter(new File(filenameCSV))) {

			StatefulBeanToCsv<MovieProjection> btc = new StatefulBeanToCsvBuilder<MovieProjection>(in)
					.withApplyQuotesToAll(false).withSeparator(',').build();
			btc.write(mp);

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (CsvDataTypeMismatchException e) {
			e.printStackTrace();
		} catch (CsvRequiredFieldEmptyException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		return mp;
	}

}
