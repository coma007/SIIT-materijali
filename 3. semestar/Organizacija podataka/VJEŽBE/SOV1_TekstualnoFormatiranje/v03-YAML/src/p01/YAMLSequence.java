package p01;

import java.util.List;

import org.yaml.snakeyaml.Yaml;

public class YAMLSequence {
	
	public static void main(String[] args) {
		
		Yaml y = new Yaml();
		
		String doc = "\n- A\n- B\n- C";
		@SuppressWarnings("unchecked")
		List<String> list = (List<String>) y.load(doc);
		System.out.println(list);
	}

}
