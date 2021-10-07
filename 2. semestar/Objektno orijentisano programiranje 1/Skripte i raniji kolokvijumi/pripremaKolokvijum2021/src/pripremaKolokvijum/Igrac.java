package pripremaKolokvijum;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Igrac {

	private String ime;
	private String prezime;
	private LocalDate datum;
	private String klub;
	private double poeni;
	private double skokovi;
	private double asistencije;
	
	public Igrac() {
	}

	public Igrac(String ime, String prezime, LocalDate datum, String klub, double poeni, double skokovi,
			double asistencije) {
		super();
		this.ime = ime;
		this.prezime = prezime;
		this.datum = datum;
		this.klub = klub;
		this.poeni = poeni;
		this.skokovi = skokovi;
		this.asistencije = asistencije;
	}
	
	public Igrac(String ime, String prezime,String klub, double poeni, double skokovi,
			double asistencije) {
		super();
		this.ime = ime;
		this.prezime = prezime;
		this.klub = klub;
		this.poeni = poeni;
		this.skokovi = skokovi;
		this.asistencije = asistencije;
	}

	public String getIme() {
		return ime;
	}

	public void setIme(String ime) {
		this.ime = ime;
	}

	public String getPrezime() {
		return prezime;
	}

	public void setPrezime(String prezime) {
		this.prezime = prezime;
	}

	public LocalDate getDatum() {
		return datum;
	}

	public void setDatum(LocalDate datum) {
		this.datum = datum;
	}

	public String getKlub() {
		return klub;
	}

	public void setKlub(String klub) {
		this.klub = klub;
	}

	public double getPoeni() {
		return poeni;
	}

	public void setPoeni(double poeni) {
		this.poeni = poeni;
	}

	public double getSkokovi() {
		return skokovi;
	}

	public void setSkokovi(double skokovi) {
		this.skokovi = skokovi;
	}

	public double getAsistencije() {
		return asistencije;
	}

	public void setAsistencije(double asistencije) {
		this.asistencije = asistencije;
	}
	
	
	
	@Override
	public String toString() {
		return "Igrac [ime=" + ime + ", prezime=" + prezime + ", datum=" + datum + ", klub=" + klub + ", poeni=" + poeni
				+ ", skokovi=" + skokovi + ", asistencije=" + asistencije + "]";
	}

	public static void main(String[] args) throws IOException {
		
		
		try {
			
		} catch (Exception e) {
			// TODO: handle exception
		}
		BufferedReader in = new BufferedReader(new InputStreamReader(new FileInputStream("./src/igraci.oop1"), "utf-8"));

		String line;
		while ((line = in.readLine()) != null) {
			String[] data = line.split(";");
			String ime = data[0];
			String prezime = data[1];
			DateTimeFormatter formatTime = DateTimeFormatter.ofPattern("dd-MM-yyyy");
			LocalDate datum = LocalDate.parse(data[2], formatTime);
			String klub = data[3];
			double poeni = Double.parseDouble(data[4]);
			double skokovi = Double.parseDouble(data[5]);
			double asistencije = Double.parseDouble(data[6]);
			Igrac i = new Igrac(ime, prezime, datum, klub, poeni, skokovi, asistencije);
			System.out.println(i);
			System.out.println(line);
		}
		
		
		
		
	}
	
	
	
	
}
