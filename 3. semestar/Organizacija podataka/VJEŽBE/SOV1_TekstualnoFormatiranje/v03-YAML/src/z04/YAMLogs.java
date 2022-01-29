package z04;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import types.log.Log;

public class YAMLogs {

	static String filename = "resources/log.yaml";
	static String fileWarn = "resources/log_warn.yaml";
	static String fileErr = "resources/log_error.yaml";
	
	public static void main(String[] args) {
		
		List<Log> logs = read();
		sortFiles(logs);
		
	}

	private static void sortFiles(List<Log> logs) {
		
		List<String> errors = new ArrayList<String>();
		List<String> warnings = new ArrayList<String>();
		
		for (Log l : logs) {
			if (l.getWarning() == null) {
				errors.add(l.getFatal());
			}
			else {
				warnings.add(l.getWarning());
			}
		}
		writeAll(errors, fileErr);
		writeAll(warnings, fileWarn);
		
	}

	private static void writeAll(List<String> mess, String file) {
		
		Yaml y = new Yaml();
		try (PrintWriter out = new PrintWriter(new File(file))) {
			y.dump(mess, out);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	private static List<Log> read() {

		List<Log> logs = new ArrayList<Log>();
		Yaml y = new Yaml(new Constructor(Log.class));
		try (InputStream in = new FileInputStream(new File(filename))) {
			for (Object l: y.loadAll(in)) {
				logs.add((Log) l);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return logs;
	}
	
}
