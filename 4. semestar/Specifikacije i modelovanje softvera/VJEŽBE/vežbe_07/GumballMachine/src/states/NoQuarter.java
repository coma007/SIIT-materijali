package states;

public class NoQuarter extends State {

	private static State instance = null;

	public static State Instance() {
		if (instance == null) {
			instance = new NoQuarter();
		}
		return instance;
	}
}
