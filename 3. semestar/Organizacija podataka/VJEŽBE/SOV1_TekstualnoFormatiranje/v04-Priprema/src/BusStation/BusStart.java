package BusStation;

import java.util.Date;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.opencsv.bean.CsvBindByPosition;
import com.opencsv.bean.CsvDate;

public class BusStart {
	
	@CsvBindByPosition(position = 0)
	public String id;
	@CsvBindByPosition(position = 1)
	public String from;
	@CsvBindByPosition(position = 2)
	public String to;
	@CsvBindByPosition(position = 3)
	@CsvDate(value = "dd.mm.yyyy.")
	@JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "dd.MM.yyyy.")
	public Date date;
	@CsvBindByPosition(position = 4)
	@CsvDate(value = "hh:mm")
	@JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "hh:mm")
	public Date timeDeparture;
	@CsvBindByPosition(position = 5)
	@CsvDate(value = "hh:mm")
	@JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "hh:mm")
	public Date timeArrival;
	@CsvBindByPosition(position = 6)
	public int peron;
	@CsvBindByPosition(position = 7)
	public double price;
	@CsvBindByPosition(position = 8)
	public int selled;

	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getFrom() {
		return from;
	}
	public void setFrom(String from) {
		this.from = from;
	}
	public String getTo() {
		return to;
	}
	public void setTo(String to) {
		this.to = to;
	}
	public Date getDate() {
		return date;
	}
	public void setDate(Date date) {
		this.date = date;
	}
	public Date getTimeDeparture() {
		return timeDeparture;
	}
	public void setTimeDeparture(Date timeDeparture) {
		this.timeDeparture = timeDeparture;
	}
	public Date getTimeArrival() {
		return timeArrival;
	}
	public void setTimeArrival(Date timeArrival) {
		this.timeArrival = timeArrival;
	}
	public int getPeron() {
		return peron;
	}
	public void setPeron(int peron) {
		this.peron = peron;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}
	public int getSelled() {
		return selled;
	}
	public void setSelled(int selled) {
		this.selled = selled;
	}
	@Override
	public String toString() {
		return "BusStart [id=" + id + ", from=" + from + ", to=" + to + ", date=" + date + ", timeDeparture="
				+ timeDeparture + ", timeArrival=" + timeArrival + ", peron=" + peron + ", price=" + price + ", selled="
				+ selled + "]";
	}
	
	
	
	public BusStart() {
		super();
	}
	public BusStart(String id, String from, String to, Date date, Date timeDeparture, Date timeArrival, int peron,
			double price, int selled) {
		this.id = id;
		this.from = from;
		this.to = to;
		this.date = date;
		this.timeDeparture = timeDeparture;
		this.timeArrival = timeArrival;
		this.peron = peron;
		this.price = price;
		this.selled = selled;
	}
	
	

}
