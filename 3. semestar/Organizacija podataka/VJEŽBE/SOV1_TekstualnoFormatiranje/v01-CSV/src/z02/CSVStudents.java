package z02;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Reader;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.opencsv.CSVWriter;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

import types.student.Student;
import types.student.StudentScore;

public class CSVStudents {

	public static String filename = "resources/students.csv";

	public static void main(String[] args) {

		List<StudentScore> scores = read();
		Map<String, Student> students = new HashMap<String, Student>();

		for (StudentScore score : scores) {
			if (students.get(score.getIndex()) == null) {
				Student s = new Student();
				s.setFname(score.getFname());
				s.setIndex(score.getIndex());
				s.setLname(score.getLname());
				students.put(s.getIndex(), s);

			}
		}

		writeGrade(students, scores, "resources/students6.csv", 6);
		writeGrade(students, scores, "resources/students7.csv", 7);
		writeGrade(students, scores, "resources/students8.csv", 8);
		writeGrade(students, scores, "resources/students9.csv", 9);
		writeGrade(students, scores, "resources/students10.csv", 10);
		
		writeAvg(students, scores, "resources/studentsAvg.csv");

	}

	private static void writeAvg(Map<String, Student> students, List<StudentScore> scores, String string) {
		Map<Student, Integer[]> st = new HashMap<Student, Integer[]>();
		for (StudentScore ss : scores) {
			if(st.get(students.get(ss.getIndex())) == null) {
				Integer[] i = {1, ss.getGrade()};
				st.put(students.get(ss.getIndex()), i);
			}
			else {
				Integer[] i = st.get(students.get(ss.getIndex()));
				i[0]++;
				i[1] += ss.getGrade();
				st.put(students.get(ss.getIndex()), i);
			}
		}
		try (CSVWriter w = new CSVWriter(new FileWriter(new File(string)))) {
			for (Student s : st.keySet()) {
				String[] str = { s.getIndex(), s.getFname(), s.getLname(), st.get(s)[0].toString(), "" + ((double) st.get(s)[1]/(double)st.get(s)[0]) };
				w.writeNext(str, false);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static void writeGrade(Map<String, Student> students, List<StudentScore> scores, String string, int grade) {

		Map<Student, Integer> st = new HashMap<Student, Integer>();
		for (StudentScore ss : scores) {
			if (ss.getGrade() == grade) {
				if (st.get(students.get(ss.getIndex())) == null) {
					st.put(students.get(ss.getIndex()), 1);
				} else {
					st.put(students.get(ss.getIndex()), st.get(students.get(ss.getIndex())) + 1);
				}
			}
		}
		try (CSVWriter w = new CSVWriter(new FileWriter(new File(string)))) {
			for (Student s : st.keySet()) {
				String[] str = { s.getIndex(), s.getFname(), s.getLname(), st.get(s).toString() };
				w.writeNext(str, false);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static List<StudentScore> read() {

		List<StudentScore> scores = null;
		try (Reader r = new FileReader(new File(filename))) {
			CsvToBean<StudentScore> sc = new CsvToBeanBuilder<StudentScore>(r).withType(StudentScore.class)
					.withSeparator(',').withSkipLines(0).build();
			scores = sc.parse();
			for (StudentScore ss : scores) {
				System.out.println(ss);
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return scores;
	}

}
