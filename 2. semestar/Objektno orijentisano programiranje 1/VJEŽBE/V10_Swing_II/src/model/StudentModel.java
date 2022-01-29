package model;

import javax.swing.table.AbstractTableModel;

import entity.Student;
import manage.StudentManager;

public class StudentModel extends AbstractTableModel {
	private static final long serialVersionUID = 173122351138550735L;
	private StudentManager studMng;
	private String[] columnNames = { "Id", "Ime", "Prezime", "Indeks" };

	public StudentModel(StudentManager mng) {
		this.studMng = mng;
	}

	@Override
	public int getRowCount() {
		return studMng.getStudenti().size();
	}

	@Override
	public int getColumnCount() {
		return columnNames.length;
	}

	@Override
	public Object getValueAt(int rowIndex, int columnIndex) {
		Student s = studMng.getStudenti().get(rowIndex);
		switch (columnIndex) {
		case 0:
			return s.getId();
		case 1:
			return s.getIme();
		case 2:
			return s.getPrezime();
		case 3:
			return s.getIndeks();
		default:
			return null;
		}

	}

	@Override
	public String getColumnName(int column) {
		return this.columnNames[column];
	}

	@Override
	public Class<?> getColumnClass(int columnIndex) {
		return this.getValueAt(0, columnIndex).getClass();
	}

}
