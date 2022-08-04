#include <iostream>
#include "MyString.h"

using namespace std;

typedef MyString String;

//void displayreverse(string student)
//{
//	// 6) .legth()
//	int stringlen = student.length();
//	for (int i = stringlen-1; i >= 0; i--)
//		cout << student[i];
//}

int main(int argc, char** argv)
{
	char c = 'a';

	// 1) Constructors
	cout << "\n--------------------------------------------------\n";
	cout << "Testing constructor without parameters" << endl;
	String s1;

	cout << "\n--------------------------------------------------\n";
	cout << "Testing constructor with parameters" << endl;
	String s2("abc");


	cout << "\n--------------------------------------------------\n";
	cout << "Testing copy constructor" << endl;
	String s3(s2);

	// 2) =
	cout << "\n--------------------------------------------------\n";
	cout << "Testing operator \"=\"" << endl;
	s1 = c;
	s2 = "string";
	s3 = s2;

	// 3) << and >>
	cout << "\n--------------------------------------------------\n";
	cout << "Testing operator \"<<\"" << endl;
	cout << "s1: " << s1 << endl;
	cout << "s2: " << s2 << endl;
	cout << "s3: " << s3 << endl;

	cout << "\n--------------------------------------------------\n";
	cout << "Testing operator \">>\"" << endl;
	String s4;
	cout << "Enter value for \"s4\": ";
	cin >> s4;
	cout << "s4: " << s4 << endl;

	// 4) []
	cout << "\n--------------------------------------------------\n";
	cout << "Testing operator \"[]\"" << endl;
	cout << "s2: " << s2 << endl;
	cout << "s2[3]: " << s2[3] << endl;
	cout << "reverse s2: ";
	//displayReverse(s2);
	cout << endl;

	// 5) +
	cout << "\n--------------------------------------------------\n";
	cout << "Testing operator \"+\"" << endl;
	cout << "s3: " << s3 << endl;
	cout << "s4: " << s4 << endl;

	String s;

	s = s4 + s3;
	cout << "s = s4 + s3\t: " << s << endl;

	s = s4 + "qwer";
	cout << "s = s4 + \"qwer\"\t: " << s << endl;

	s = s4 + 'o';
	cout << "s = s4 + \'o\'\t: " << s << endl;

	s = "jkl" + s4;
	cout << "s = \"jkl\" + s4\t: " << s << endl;

	//s = 'b' + s4;
	//cout << "s = \'b\' + s4\t: " << s << endl;

	// END
	cout << "\n--------------------------------------------------\n";
	return 0;
}
