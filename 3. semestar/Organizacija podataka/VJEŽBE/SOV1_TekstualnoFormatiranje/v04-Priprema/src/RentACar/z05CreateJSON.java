package RentACar;

import java.io.File;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

public class z05CreateJSON {
	
	static String filename = "resources/car/rents.json";
	
	public static void main(String[] args) throws ParseException {
		
		List<Car> rents = generateCars(); 
		writeJSON(rents);
		
	}

	private static void writeJSON(List<Car> rents) {

		ObjectMapper om = new ObjectMapper();
		om.enable(SerializationFeature.INDENT_OUTPUT);
		om.setDateFormat(new SimpleDateFormat("dd.MM.yyyy"));
		
			
			try {
				om.writeValue(new File(filename), rents);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		
	}

	private static List<Car> generateCars() throws ParseException {
		
		List<Car> rents = new ArrayList<Car>();
		SimpleDateFormat sdf = new SimpleDateFormat("dd.MM.yyyy.");
		rents.add(new Car("111", "Novi Sad", sdf.parse("12.12.2020."), sdf.parse("12.01.2021."), 1000., 3000., new Person("Marko", "Mitic", "123123123")));
		rents.add(new Car("222", "Novi Sad", sdf.parse("10.12.2020."), sdf.parse("12.01.2021."), 900., 1200., new Person("Mihailo", "Milosevic", "392929292")));
		rents.add(new Car("333", "Novi Sad", sdf.parse("05.12.2020."), sdf.parse("12.12.2020."), 1000., 500., new Person("Ivko", "Ivankovic", "654654465")));
		rents.add(new Car("444", "Novi Sad", sdf.parse("08.12.2020."), sdf.parse("12.02.2021."), 1500., 700., new Person("Marko", "Jelica", "789879878")));
		rents.add(new Car("555", "Novi Sad", sdf.parse("12.05.2020."), sdf.parse("12.01.2021."), 3000., 800., new Person("Marica", "Mihail", "165895354")));
		rents.add(new Car("666", "Novi Sad", sdf.parse("12.07.2020."), sdf.parse("13.07.2020."), 400., 1200., new Person("Ana", "Tanasic", "687219548")));
		rents.add(new Car("777", "Novi Sad", sdf.parse("03.12.2020."), sdf.parse("02.01.2021."), 100., 500., new Person("Karla", "Vatic", "658765155")));
		rents.add(new Car("888", "Novi Sad", sdf.parse("11.12.2020."), sdf.parse("12.12.2020."), 1559., 1565., new Person("Borislav", "Kikic", "798651623")));
		
		return rents;
	}

}
