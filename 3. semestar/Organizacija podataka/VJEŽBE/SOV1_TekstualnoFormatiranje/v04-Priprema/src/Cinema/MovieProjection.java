package Cinema;

import com.opencsv.bean.CsvBindByPosition;

public class MovieProjection {
	
	@CsvBindByPosition(position = 0)
	public String id;
	@CsvBindByPosition(position = 1)
	public String movie;
	@CsvBindByPosition(position = 2)
	public int length;
	@CsvBindByPosition(position = 3)
	public String roomId;
	@CsvBindByPosition(position = 4)
	public String roomName;
	@CsvBindByPosition(position = 5)
	public int roomCapacity;
	@CsvBindByPosition(position = 6)
	public double price;
	
	
	public MovieProjection() {
	}
	
	public MovieProjection(Movie m, Room r, double price) {
		this.id = m.getId();
		this.movie = m.getMovie();
		this.length = m.getLength();
		this.roomId = r.getRoomId();
		this.roomName = r.getRoomName();
		this.roomCapacity = r.getRoomCapacity();
		this.price = price;
	}
	
	public MovieProjection(String id, String movie, int length, String roomId, String roomName, int roomCapacity,
			double price) {
		this.id = id;
		this.movie = movie;
		this.length = length;
		this.roomId = roomId;
		this.roomName = roomName;
		this.roomCapacity = roomCapacity;
		this.price = price;
	}

	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getMovie() {
		return movie;
	}
	public void setMovie(String movie) {
		this.movie = movie;
	}
	public String getRoomId() {
		return roomId;
	}
	public void setRoomId(String roomId) {
		this.roomId = roomId;
	}
	public String getRoomName() {
		return roomName;
	}
	public void setRoomName(String roomName) {
		this.roomName = roomName;
	}
	public int getRoomCapacity() {
		return roomCapacity;
	}
	public void setRoomCapacity(int roomCapacity) {
		this.roomCapacity = roomCapacity;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}

	public int getLength() {
		return length;
	}

	public void setLength(int length) {
		this.length = length;
	}

	@Override
	public String toString() {
		return "MovieProjection [id=" + id + ", movie=" + movie + ", length=" + length + ", roomId=" + roomId
				+ ", roomName=" + roomName + ", roomCapacity=" + roomCapacity + ", price=" + price + "]";
	}
	
	
	

}
