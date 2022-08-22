package states;

public class GumballSold extends State {

	private static State instance = null;

	public static State Instance() {
		if (instance == null) {
			instance = new GumballSold();
		}
		return instance;
	}
}