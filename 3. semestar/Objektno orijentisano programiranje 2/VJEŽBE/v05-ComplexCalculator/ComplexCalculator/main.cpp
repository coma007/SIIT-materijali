#include <iostream>
#include "MyComplex.h"
#include <fstream>
#include <string>
#include <vector>

using namespace std;

Complex createComplex(string operand) {

	double real = 0;
	double imag = 0;

	bool doingReal = true;
	string tmp = "";
	int sign = 1;
	for (char c : operand) {
		switch (c) {
		case '+':
			if (doingReal && tmp != "") {
				real = stod(tmp) * sign;
				doingReal = false;
			}
			sign = 1;
			tmp = "";
			break;
		case '-':
			if (doingReal && tmp != "") {
				real = stod(tmp) * sign;
				doingReal = false;
			}
			sign = -1;
			tmp = "";
			break;
		case 'i':
			imag = stod(tmp) * sign;
			break;

		default:
			tmp += c;
		}
	}

	return Complex(real, imag);

}

Complex parse(vector<string> expression) {

	string operand1 = expression[0];
	string operation = expression[1];
	string operand2 = expression[2];

	Complex a = createComplex(operand1);
	Complex b = createComplex(operand2);
	Complex res;

	if (operation == "ADD") {
		res = a + b;
	}
	else if (operation == "MUL") {
		res = a * b;
	}
	else if (operation == "SUB") {
		res = a - b;
	}

	return res;


}

string read(string filename) {

	string in;
	ifstream readfile(filename);

	vector<string> expression;
	string tmp;

	Complex res;
	string toWrite;

	while (getline(readfile, in)) {
		tmp = "";
		for (char c : in) {

			switch (c) {
			case ' ':
				expression.push_back(tmp);
				tmp = "";
				break;
			case ';':
				expression.push_back(tmp);
				res = parse(expression);
				toWrite += "= (" + to_string(res.getReal()) + ", " + to_string(res.getImag()) + "i)" + "\n";
				expression.clear();
				break;
			default:
				tmp += c;
			}
		}
	}

	readfile.close();

	return toWrite;
}


void write(string toWrite, string filename) {
	
	ofstream writeFile("o_"+filename);

	writeFile << toWrite;

	writeFile.close();

}



int main() {

	int len;
	cout << "Input number of files: ";
	cin >> len;
	string* filenames = new string[10];
	string toWrite;

	for (int i = 0; i < len; i++) {
		cout << "Input filename: ";
		cin >> filenames[i];
	}
	
	for (int i = 0; i < len; i++) {
		toWrite = read(filenames[i]);
		write(toWrite, filenames[i]);
	}
	
	return 0;
}