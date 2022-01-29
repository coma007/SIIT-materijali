package RentACar;

import java.util.Date;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.opencsv.bean.CsvBindByPosition;
import com.opencsv.bean.CsvDate;

public class Car implements Comparable<Car>{
	
	@CsvBindByPosition(position = 0)
	public String id;
	@CsvBindByPosition(position = 1)
	public String place;
	@CsvBindByPosition(position = 2)
	@CsvDate(value = "dd.MM.yyyy.")
	@JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "dd.MM.yyyy.")
	public Date start;
	@CsvBindByPosition(position = 3)
	@CsvDate(value = "dd.MM.yyyy.")
	@JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "dd.MM.yyyy.")
	public Date end;
	@CsvBindByPosition(position = 4)
	public double km;
	@CsvBindByPosition(position = 5)
	public double price;
	@CsvBindByPosition(position = 6)
	public long days;
	@CsvBindByPosition(position = 7)
	public Person person;
	
	
	public Car() {
	}
	
	public Car(String id, String place, Date start, Date end, double km, double price, Person person) {
		this.id = id;
		this.place = place;
		this.start = start;
		this.end = end;
		this.km = km;
		this.price = price;
		this.person = person;
		this.days = Math.abs(end.getTime() - start.getTime()) / 24 / 60 / 60 / 1000;
		
		person.setTotal(person.getTotal() + days*price);
		person.setAvgDays(person.getAvgDays() + days);
	}
	
	@Override
	public String toString() {
		return "Car [id=" + id + ", place=" + place + ", start=" + start + ", end=" + end + ", km=" + km + ", price="
				+ price + ", days=" + days + ", person=" + person + "]";
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPlace() {
		return place;
	}
	public void setPlace(String place) {
		this.place = place;
	}
	public Date getStart() {
		return start;
	}
	public void setStart(Date start) {
		this.start = start;
	}
	public Date getEnd() {
		return end;
	}
	public void setEnd(Date end) {
		this.end = end;
	}
	public double getKm() {
		return km;
	}
	public void setKm(double km) {
		this.km = km;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}
	public long getDays() {
		return days;
	}
	public void setDays(long days) {
		this.days = days;
	}
	public Person getPerson() {
		return person;
	}
	public void setPerson(Person person) {
		this.person = person;
	}

	@Override
	public int compareTo(Car o) {
		if (km > o.getKm()) return 1;
		if (km < o.getKm()) return -1;
		return 0;
	}
	
	
	

}
