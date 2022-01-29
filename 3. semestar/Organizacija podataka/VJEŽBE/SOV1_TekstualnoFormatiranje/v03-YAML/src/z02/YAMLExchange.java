package z02;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import types.invoice.Invoice;
import types.invoice.Product;

public class YAMLExchange {

	static String filename = "resources/invoice.yaml";
	static String filenameX = "resources/invoice_";
	static String filenameEx = "resources/exchange.yaml";

	@SuppressWarnings("unchecked")
	public static void main(String[] args) {

		Yaml y = new Yaml(new Constructor(Invoice.class));

		Invoice i = null;
		Map<String, Integer> ex = new HashMap<String, Integer>();
		try (InputStream in = new FileInputStream(new File(filename))) {

			i = (Invoice) y.load(in);

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		Yaml yEx = new Yaml(new Constructor(HashMap.class));
		try (InputStream in = new FileInputStream(new File(filenameEx))) {

			ex = (HashMap<String, Integer>) yEx.load(in);

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		System.out.println("Exchange Office: ");
		int count = 1;
		for (String s: ex.keySet()) {
			System.out.println(count + " - " + s + " = " + ex.get(s) + " RSD");
			count++;
		}
		System.out.println("Chose option: ");
		
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int choice = sc.nextInt();
		
		count = 1;
		double course = 0;
		String valute = ".yaml";
		
		for (String s: ex.keySet()) {
			if (count == choice) {
				course = (double) 1 / ex.get(s);
				valute = s + valute;
			}
			count++;
		}
		filenameX += valute;
		
		for (Product p : i.getProduct()) {
			p.setPrice(p.getPrice() * course);
		}
		
		i.setTax(i.getTax() * course);
		i.setTotal(i.getTotal() * course);
		
		try (PrintWriter out = new PrintWriter(new File(filenameX))) {
			
			Yaml k = new Yaml();
			k.dump(i, out);
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}		
	

}
