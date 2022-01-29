package BusStation;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Reader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.yaml.snakeyaml.Yaml;

import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

public class z02YAMLBestBusRelations {

	static String filename = "resources/bus/bus.csv";
	static String filenameNew = "resources/bus/busBest.yaml";

	public static void main(String[] args) {

		List<BusStart> all = readCSV();
		BusStart bestFrequency = getFrequency(all);
		BusStart maxTime = getTime(all);
		BusStart bestMoney = getMoney(all);
		
		Map<String, BusStart> best = new HashMap<String, BusStart>();
		best.put("Najveci broj polazaka", bestFrequency);
		best.put("Najduze trajanje", maxTime);
		best.put("Najbolja zarada", bestMoney);
		
		toYaml(best);

	}

	private static void toYaml(Map<String, BusStart> best) {
		
		Yaml y = new Yaml();
		try (PrintWriter out = new PrintWriter(new File(filenameNew))) {
			y.dump(best, out);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	private static BusStart getMoney(List<BusStart> all) {
		
		BusStart maxi = null;
		double num = 0;
		for (BusStart b : all) {
			if (b.getPrice() * b.getSelled() > num) {
				maxi = b;
				num = b.getPrice() * b.getSelled();
			}
		}
		return maxi;
		
	}

	private static BusStart getTime(List<BusStart> all) {
		
		BusStart maxi = null;
		int num = 0;
		for (BusStart b : all) {
			if (b.getTimeDeparture().getTime() - b.getTimeArrival().getTime() > num) {
				maxi = b;
				num = (int) (b.getTimeArrival().getTime() - b.getTimeDeparture().getTime());
			}
		}
		return maxi;
	}

	private static BusStart getFrequency(List<BusStart> all) {

		Map<String, Integer> fr = new HashMap<String, Integer>();

		for (BusStart b : all) {
			if (fr.get(b.getId()) == null) {
				fr.put(b.getId(), 1);
			} else {
				fr.put(b.getId(), fr.get(b.getId()) + 1);
			}
		}

		BusStart maxi = null;
		int num = 0;
		for (BusStart b : all) {
			if (fr.get(b.getId()) > num) {
				maxi = b;
				num = fr.get(b.getId());
			}
		}
		return maxi;
	}

	public static List<BusStart> readCSV() {

		List<BusStart> bs = new ArrayList<BusStart>();
		try (Reader in = new FileReader(new File(filename))) {
			CsvToBean<BusStart> ctb = new CsvToBeanBuilder<BusStart>(in).withType(BusStart.class).withSeparator(',').build();
			bs = ctb.parse();
			
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return bs;
	}

}
