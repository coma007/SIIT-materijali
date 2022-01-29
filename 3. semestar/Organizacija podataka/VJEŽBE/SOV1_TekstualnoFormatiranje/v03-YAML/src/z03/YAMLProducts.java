package z03;

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

import types.invoice.Invoice;
import types.invoice.Product;

public class YAMLProducts {
	
	static String filename = "resources/invoice.yaml";
	
	public static void main(String[] args) {
		
		List<Product> products = readFile();
		writeFiles(products);
		
	}

	private static void writeFiles(List<Product> products) {
		Yaml y = new Yaml();
		for (int i = 1; i <= products.size(); i++) {
			try (PrintWriter out = new PrintWriter(new File("resources/invoice_" + i + ".yaml"))) {
				y.dump(products.get(i-1), out);
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}
	}

	private static List<Product> readFile() {
	
		List<Product> prs = new ArrayList<Product>();
		Invoice i = null;
		
		Yaml y = new Yaml(new Constructor(Invoice.class));
		
		try (InputStream in = new FileInputStream(new File(filename))) {
			
			i =  (Invoice) y.load(in);
			
			for (Product p : i.getProduct()) {
				p.setTax(i.getTax() / i.getTotal() * p.getQuantity() * p.getPrice());
				prs.add(p);
			}
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return prs;
	}
	
}
