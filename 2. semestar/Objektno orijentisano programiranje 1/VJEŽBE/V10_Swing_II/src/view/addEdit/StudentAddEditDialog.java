package view.addEdit;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import entity.Predmet;
import entity.Student;
import manage.StudentManager;
import net.miginfocom.swing.MigLayout;
import view.StudentTableFrame;

public class StudentAddEditDialog extends JDialog {
	private static final long serialVersionUID = -5247231764310200252L;
	private StudentManager studMng;
	private Student editS;
	private JFrame parent;
	
	// Jedan isti dijalog za Add i Edit
	public StudentAddEditDialog(JFrame parent, StudentManager studMng, Student editStudent) {
		super(parent, true);
		this.parent = parent;
		if (editStudent != null) {
			setTitle("Izmena studenta");
		} else {
			setTitle("Dodavanje studenta");
		}
		this.studMng = studMng;
		this.editS = editStudent;

		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setLocationRelativeTo(null);
		setResizable(false);
		initGUI();
		pack();
	}

	private void initGUI() {
		// 1. nacin sa MigLayout - dosta laksi
		MigLayout ml = new MigLayout("wrap 3", "[][][]", "[]10[]10[]10[]20[]");
		setLayout(ml);

		JLabel lblId = new JLabel("Id");
		add(lblId);

		JTextField txtId = new JTextField(20);
		add(txtId, "span 2");

		JLabel lblIme = new JLabel("Ime");
		add(lblIme);

		JTextField txtIme = new JTextField(20);
		add(txtIme, "span 2");

		JLabel lblPrezime = new JLabel("Prezime");
		add(lblPrezime);

		JTextField txtPrezime = new JTextField(20);
		add(txtPrezime, "span 2");

		JLabel lblIndeks = new JLabel("Indeks");
		add(lblIndeks);

		JTextField txtIndeks = new JTextField(20);
		add(txtIndeks, "span 2");

		// prazno za prvu kolonu
		add(new JLabel());

		JButton btnCancel = new JButton("Cancel");
		add(btnCancel);

		JButton btnOK = new JButton("OK");
		add(btnOK);

		/*
		 * // 2. nacin sa GridBagLayout 
		 * GridBagLayout gbl = new GridBagLayout();
		 * setLayout(gbl);
		 * 
		 * GridBagConstraints con = new GridBagConstraints(); JLabel lblId = new
		 * JLabel("Id"); con.fill = GridBagConstraints.HORIZONTAL; con.gridwidth = 1;
		 * con.weightx = 0.5; con.gridx = 0; con.gridy = 0; con.insets = new Insets(10,
		 * 10, 10, 10); add(lblId, con);
		 * 
		 * JTextField txtId = new JTextField(20); con.fill =
		 * GridBagConstraints.HORIZONTAL; con.gridwidth = 2; con.weightx = 0.5;
		 * con.gridx = 1; con.gridy = 0; add(txtId, con);
		 * 
		 * 
		 * JLabel lblIme = new JLabel("Ime"); con.gridwidth = 1; con.weightx = 0.5;
		 * con.gridx = 0; con.gridy = 1; con.insets = new Insets(0, 10, 10, 10);
		 * add(lblIme, con);
		 * 
		 * JTextField txtIme = new JTextField(20); con.fill =
		 * GridBagConstraints.HORIZONTAL; con.gridwidth = 2; con.weightx = 0.5;
		 * con.gridx = 1; con.gridy = 1; add(txtIme, con);
		 * 
		 * 
		 * JLabel lblPrezime = new JLabel("Prezime"); con.gridwidth = 1; con.weightx =
		 * 0.5; con.gridx = 0; con.gridy = 2; //con.insets = new Insets(10, 10, 10, 10);
		 * add(lblPrezime, con);
		 * 
		 * JTextField txtPrezime = new JTextField(20); con.fill =
		 * GridBagConstraints.HORIZONTAL; con.gridwidth = 2; con.weightx = 0.5;
		 * con.gridx = 1; con.gridy = 2; add(txtPrezime, con);
		 * 
		 * JLabel lblIndeks = new JLabel("Indeks"); con.gridwidth = 1; con.weightx =
		 * 0.5; con.gridx = 0; con.gridy = 3; //con.insets = new Insets(10, 10, 10, 10);
		 * add(lblIndeks, con);
		 * 
		 * JTextField txtIndeks = new JTextField(20); con.fill =
		 * GridBagConstraints.HORIZONTAL; con.gridwidth = 2; con.weightx = 0.5;
		 * con.gridx = 1; con.gridy = 3; add(txtIndeks, con);
		 * 
		 * 
		 * JButton btnCancel = new JButton("Cancel"); btnCancel.setPreferredSize(new
		 * Dimension(30, 25)); con.fill = GridBagConstraints.HORIZONTAL; con.gridwidth =
		 * 1; //con.weightx = 0.8; con.gridx = 1; con.gridy = 4; add(btnCancel, con);
		 * 
		 * JButton btnOK = new JButton("OK"); btnOK.setPreferredSize(new Dimension(30,
		 * 25)); con.gridwidth = 1; //con.weightx = 1.0; con.gridx = 2; con.gridy = 4;
		 * //con.insets = new Insets(10, 10, 10, 10); add(btnOK, con);
		 * 
		 */

		if (editS != null) {
			// popuni polja vrednostima
			txtId.setText(editS.getId() + "");
			txtIme.setText(editS.getIme());
			txtPrezime.setText(editS.getPrezime());
			txtIndeks.setText(editS.getIndeks());
			
			// Primer ispisa predmeta
			// TO DO: Radi bolje organizacije elemenata GUI-a, ovo staviti iznad dugmica Ok i Cancel			
			if (editS.getPredmeti() != null && editS.getPredmeti().size() > 0) {
				JTextArea textArea = new JTextArea(editS.getPredmeti().size() + 1, 10);
				JScrollPane scrollPane = new JScrollPane(textArea);
				textArea.setEditable(false);

				for (Predmet p : editS.getPredmeti()) {
					textArea.append(p.getNaziv() + "\n");
				}

				JLabel lblPredmeti = new JLabel("Predmeti:");
				add(lblPredmeti);

				add(scrollPane, "span 2");
			}

		}

		btnOK.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				int id = Integer.parseInt(txtId.getText().trim());
				String ime = txtIme.getText().trim();
				String prezime = txtPrezime.getText().trim();
				String indeks = txtIndeks.getText().trim();
				
				// odve se odvaja GUI od funkcionalnosti Manager-a
				// ne mesati logiku app i funkcionalnosti sa GUI-om !
				if (editS != null) {
					studMng.edit(editS.getId(), ime, prezime, indeks);
				} else {
					studMng.add(id, ime, prezime, indeks);
				}
				((StudentTableFrame) parent).refreshData();
				StudentAddEditDialog.this.dispose();
			}
		});

		btnCancel.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				StudentAddEditDialog.this.dispose();
			}
		});
	}

}
