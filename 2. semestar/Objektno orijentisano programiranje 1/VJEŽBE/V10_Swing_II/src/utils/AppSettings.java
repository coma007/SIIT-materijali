package utils;

public class AppSettings {
	private String studentFilename, predmetFilename;
	
	
	public AppSettings(String studentFilename, String predmetFilename) {
		super();
		this.studentFilename = studentFilename;
		this.predmetFilename = predmetFilename;
	}


	public String getStudentFilename() {
		return studentFilename;
	}


	public String getPredmetFilename() {
		return predmetFilename;
	}	
	
}
