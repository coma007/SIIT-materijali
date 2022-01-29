package BusStation;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.yaml.snakeyaml.Yaml;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

public class z03YAMLJSONReturns {
	
	static String filename = "resources/bus/bus.csv";
	static String filenameYAML = "resources/bus/returns.yaml";
	static String filenameJSON = "resources/bus/noreturn.json";
	
	public static void main(String[] args) {
		
		List<BusStart> all = z02YAMLBestBusRelations.readCSV();
		List<BusStart> returns = getReturns(all);
		List<BusStart> noreturns = getNoreturns(all, returns);
		
		writeYaml(returns);
		writeJSON(noreturns);
	}

	private static void writeJSON(List<BusStart> noreturns) {
		
		ObjectMapper mp = new ObjectMapper();
		try (PrintWriter out = new PrintWriter(new FileWriter(new File(filenameJSON)))) {
			mp.enable(SerializationFeature.INDENT_OUTPUT);
			mp.writeValue(out, noreturns);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static void writeYaml(List<BusStart> returns) {
		
		Yaml y = new Yaml();
		
		try (PrintWriter out = new PrintWriter(new FileWriter(new File(filenameYAML)))) {
			y.dump(returns, out);
		} catch (IOException e) {
			e.printStackTrace();
		}
	
	}

	private static List<BusStart> getNoreturns(List<BusStart> all, List<BusStart> returns) {
		List<BusStart> bsn = new ArrayList<BusStart>();
		
		for (BusStart b : all) {
			if (!returns.contains(b)) {
				bsn.add(b);
			}
		}
		return bsn;
	}

	private static List<BusStart> getReturns(List<BusStart> all) {

		List<BusStart> bs = new ArrayList<BusStart>();
		
		Map<String, BusStart> mp = new HashMap<String, BusStart>();
		for (BusStart b : all) {
			if (mp.get(b.getId()) == null) {
				mp.put(b.getId(), b);
				bs.add(b);
				
			}
			else if (mp.get(b.getId()).getTo() == b.getFrom()){
				bs.add(b);
			}
		}
		
		return bs;
	}

}
