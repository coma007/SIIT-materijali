package z01;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import types.invoice.Invoice;

public class YAMLMod {
	
	static String filename = "resources/invoice.yaml";
	static String newfilename = "resources/invoice_mod.yaml";
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		Yaml y = new Yaml(new Constructor(Invoice.class));
		Invoice i = null;
		
		try (InputStream in = new FileInputStream(new File(filename))) {
			
			i = (Invoice) y.load(in);
			System.out.println(i);
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		System.out.println("Unesite novu adresu: ");
		String addr = sc.nextLine();
		
		i.getBillTo().getAddress().setLines(addr);
		
		try (PrintWriter out = new PrintWriter(new File(newfilename))) {
			Yaml ny = new Yaml();
			ny.dump(i, out);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		sc.close();
	}

}
