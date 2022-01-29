package p01;

import java.util.Map;

import org.yaml.snakeyaml.Yaml;

public class YAMLMap {
	
	public static void main(String[] args) {
		
		Yaml y = new Yaml();
		
		String doc = "Manufacturer: Toyota\nModel: Yaris\nYear: 2018";
		@SuppressWarnings("unchecked")
		Map<String, Object> map = (Map<String, Object>) y.load(doc);
		System.out.println(map);
	}

}
