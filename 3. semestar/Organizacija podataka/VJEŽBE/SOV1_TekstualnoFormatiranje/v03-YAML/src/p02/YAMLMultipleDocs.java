package p02;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Map;

import org.yaml.snakeyaml.Yaml;

public class YAMLMultipleDocs {
	
	static String filename = "resources/log.yaml";
	
	public static void main(String[] args) {
		
		try (InputStream in = new FileInputStream(new File(filename))) {
		
		Yaml y = new Yaml();
		
		for (Object o : y.loadAll(in)) {
			System.out.println("Data: " +  o);
			
			@SuppressWarnings("unchecked")
			Map<String, Object> map = (Map<String, Object>) o;
 			System.out.println("Time: " + map.get("Time"));
			
 			
			
		}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}

}
