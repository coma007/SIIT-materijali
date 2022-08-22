package states;

public class HasQuarter extends State {

	private static State instance = null;

	public static State Instance() {
		if (instance == null) {
			instance = new HasQuarter();
		}
		return instance;
	}
}