package manage;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import entity.Predmet;

public class PredmetManager {
	private List<Predmet> predmeti;

	private String predmetFile;

	public PredmetManager(String predmetFile) {
		super();
		this.predmetFile = predmetFile;
		this.predmeti = new ArrayList<Predmet>();
	}
	
	// metode slicno kao i u StudentManager-u

    // pronadji predmet
    public Predmet PronadjiPredmetPoId(int id)
    {
        Predmet retVal = null;
        for (int i = 0; i < predmeti.size(); i++)
        {
            Predmet pr = predmeti.get(i);
            if (pr.getId() == id)
            {
                retVal = pr;
                break;
            }
        }
        return retVal;
    }

   

	public boolean loadData() {
		try {
			BufferedReader br = new BufferedReader(new FileReader(this.predmetFile));
			String linija = null;
			while ((linija = br.readLine()) != null) {
				String[] tokeni = linija.split(",");
				this.predmeti.add(new Predmet(Integer.parseInt(tokeni[0]), tokeni[1], tokeni[2], tokeni[3]));
			}
			br.close();
		} catch (IOException e) {
			return false;
		}
		return true;
	}
	
	public boolean saveData() {
		PrintWriter pw = null;
		try {
			pw = new PrintWriter(new FileWriter(this.predmetFile, false));
			for (Predmet p : predmeti) {
				pw.println(p.toFileString());
			}
			pw.close();
		} catch (IOException e) {
			return false;
		}
		return true;
	}
}
