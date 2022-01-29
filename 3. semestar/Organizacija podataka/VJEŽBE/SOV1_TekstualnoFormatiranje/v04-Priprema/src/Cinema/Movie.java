package Cinema;

public class Movie {

	public String id;
	public String movie;
	public int length;

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

	public int getLength() {
		return length;
	}

	public void setLength(int length) {
		this.length = length;
	}

	@Override
	public String toString() {
		return "Movie [id=" + id + ", movie=" + movie + ", length=" + length + "]";
	}

	public Movie(String id, String movie, int length) {
		this.id = id;
		this.movie = movie;
		this.length = length;
	}

	public Movie() {
	}

}
