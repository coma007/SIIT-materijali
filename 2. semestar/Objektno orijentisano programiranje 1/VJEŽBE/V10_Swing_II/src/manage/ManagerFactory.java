package manage;

import utils.AppSettings;

public class ManagerFactory {
	private AppSettings appSettings;
	private StudentManager studentMng;
	private PredmetManager predmetMng;
	
	public ManagerFactory(AppSettings appSettings) {
		this.appSettings = appSettings;
		this.predmetMng = new PredmetManager(this.appSettings.getPredmetFilename());
		this.studentMng = new StudentManager(this.appSettings.getStudentFilename(), predmetMng);
	}

	public StudentManager getStudentMng() {
		return studentMng;
	}

	public PredmetManager getPredmetMng() {
		return predmetMng;
	}

	public void loadData() {
		this.predmetMng.loadData();
		this.studentMng.loadData();		
	}
	
	
	
}
