package p03;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import types.invoice.Invoice;

public class YAMLParsing {
	
	static String filename = "resources/invoice.yaml";

	public static void main(String[] args) {
		
		Invoice i = null;
		try (InputStream in = new FileInputStream(new File(filename))) {
			
			Yaml y = new Yaml(new Constructor(Invoice.class));
			
			i = (Invoice) y.load(in);

			System.out.println(i);
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	
		Yaml y = new Yaml();
		String out = y.dump(i);
		System.out.println(out);
	}
	
	
}
