package view;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

import manage.ManagerFactory;
import net.miginfocom.swing.MigLayout;

public class MainFrame extends JFrame {
	private static final long serialVersionUID = 8456560429229699542L;

	private ManagerFactory managers;

	public MainFrame(ManagerFactory managers) {
		this.managers = managers;

		loginDialog();

		mainFrame();
	}

	private void loginDialog() {
		JDialog d = new JDialog();
		d.setTitle("Prijava");
		d.setLocationRelativeTo(null);
		d.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
		d.setResizable(false);
		initLoginGUI(d);
		d.pack();
		d.setVisible(true);
	}

	private void initLoginGUI(JDialog dialog) {
		/*
		 * Malo detaljnije podesavanje MigLayout-a: Drugi parametar (string) sadrzi 2
		 * prazne uglaste zagrade jer imamo 2 kolone (ovde nista nismo podesili) Treci
		 * parametar ima onoliko uglastih zagrada koliko imamo redova (u nasem slucaju
		 * 4) Unutar zagrada mozemo detaljnije podesavati kolone i redove, dok vrednosti
		 * izmedju njih predstavljaju razmake u pikselima. Ovde smo postavili razmak od
		 * 20px izmedju 1. i 2. i izmedju 3. i 4. reda.
		 */
		MigLayout layout = new MigLayout("wrap 2", "[][]", "[]20[][]20[]");
		dialog.setLayout(layout);

		JTextField tfKorisnickoIme = new JTextField(20);
		JPasswordField pfLozinka = new JPasswordField(20);
		JButton btnOk = new JButton("OK");
		JButton btnCancel = new JButton("Cancel");

		// Ako postavimo dugme 'btnOK' kao defaul button, onda ce svaki pritisak tastera
		// Enter na tastaturi
		// Izazvati klik na njega
		dialog.getRootPane().setDefaultButton(btnOk);

		dialog.add(new JLabel("Dobrodošli. Molimo da se prijavite."), "span 2");
		dialog.add(new JLabel("Korisničko ime"));
		dialog.add(tfKorisnickoIme);
		dialog.add(new JLabel("Šifra"));
		dialog.add(pfLozinka);
		dialog.add(new JLabel());
		dialog.add(btnOk, "split 2");
		dialog.add(btnCancel);

		// Klik na Login dugme
		btnOk.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				String korisnickoIme = tfKorisnickoIme.getText().trim();
				String lozinka = new String(pfLozinka.getPassword()).trim();
				System.out.println(korisnickoIme+" "+lozinka);
				// TO DO
				// Ukoliko nesto nije uneseno, obavestimo korisnika
				// JOptionPane.showMessageDialog(null, "Niste uneli sve podatke.")
				// Provera login podataka, ispisujemo poruku ukoliko korisnik nije nadjen
				// Ukoliko su podaci ispravni, od menadzera korisnika dobijamo objekat korisnika				
				// Sakrijemo Login prozor i dispose-ujemo
				dialog.setVisible(false);
				dialog.dispose();
				// Prikazemo glavni prozor
				MainFrame.this.setVisible(true);
			}
		});
		// Cancel dugme samo sakriva trenutni prozor
		btnCancel.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				dialog.setVisible(false);
				dialog.dispose();
			}
		});

	}

	private void mainFrame() {
		this.setTitle("Studentska sluzba");
		this.setSize(500, 500);
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		this.setResizable(false);
		this.setIconImage(new ImageIcon("img/icon.png").getImage());

		initMainGUI();


	}

	private void initMainGUI() {
		JMenuBar mainMenu = new JMenuBar();

		JMenu studentiMenu = new JMenu("Meni za studente");
		JMenuItem studentiItem = new JMenuItem("Prikaži studente");
		JMenuItem predmetiItem = new JMenuItem("Prikaži predmete");

		studentiMenu.add(studentiItem);
		studentiMenu.add(predmetiItem);

		mainMenu.add(studentiMenu);
		
		// tmp
		JMenu profesoriMenu = new JMenu("Meni za profesore");
		profesoriMenu.add(new JMenuItem("TO DO"));
		profesoriMenu.add(new JMenuItem("TO DO"));
		
		mainMenu.add(profesoriMenu);
		
		this.setJMenuBar(mainMenu);

		// Klikom na stavke menija otvaraju se odgovarajuce forme za prikaz
		studentiItem.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				StudentTableFrame tf = new StudentTableFrame(MainFrame.this, managers.getStudentMng());
				tf.setVisible(true);
			}
		});
		predmetiItem.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TO DO
				JOptionPane.showMessageDialog(MainFrame.this, "Nije implementirano!","Info", JOptionPane.WARNING_MESSAGE);
			}
		});
		
		// tmp
		add(new JLabel("  Ovde na centralnom mestu glavnog prozora staviti ono sto je najbitnije za korisnika!"), BorderLayout.CENTER);
		// Npr. Za studenta su bitni ispiti, ispitni rokovi, ili ocene i prosek itd.
	}
}
