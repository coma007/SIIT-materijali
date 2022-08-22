package states;

public class OutOfGumballs extends State {

	private static State instance = null;

	public static State Instance() {
		if (instance == null) {
			instance = new OutOfGumballs();
		}
		return instance;
	}
}

