package main;

import manage.ManagerFactory;
import utils.AppSettings;
import view.MainFrame;

public class StudentskaSluzba {
	public static void main(String[] args) {
		System.out.println("Podesavanje aplikacije ...");
		// Primer klase koja ce sadrzati sva potrebna podesavanja aplikacije, za sad samo datoteka
		AppSettings appSettings = new AppSettings("./data/student.csv", "./data/predmet.csv");
		// Primer klase koja ce biti zaduzena za instanciranje Manager klasa za glavne entitete
		ManagerFactory controlers = new ManagerFactory(appSettings);
		// Metoda ce unutar sebe ucitati podatke za sve potrebne menadzere
		controlers.loadData();
		System.out.println("Pokretanje glavnog prozora");
		
		// Instanciranje glavnog prozora aplikacije koji ce dalje otvarati/zatvarati naredne prozore i dijaloge
		MainFrame main = new MainFrame(controlers);
		main.toString();
		
	}
}
