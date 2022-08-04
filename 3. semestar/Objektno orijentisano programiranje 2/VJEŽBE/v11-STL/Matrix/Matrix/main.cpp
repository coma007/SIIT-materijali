#include "Matrix.h"
#include <map>

std::map<std::string, Matrix> MapOfMatrices() {
	std::map<std::string, Matrix> mom;
	return mom;
}

int main(int argc, char** argv){
	Matrix m(1, 2);
	m.UpdateElement(0, 0, 1);
	m.UpdateElement(0, 1, 2);
	m.Print();

	std::map<std::string, Matrix> mom = MapOfMatrices();
	mom["m2"] = m;
	mom["m1"] = Matrix(2, 2);
	mom["m3"] = Matrix(1, 1);
	mom["m3"].UpdateElement(0, 0, 1);

	map<string, Matrix>::iterator i;
	for (i = mom.begin(); i != mom.end(); i++)
	{
		cout << i->first << ":" << endl;
		i->second.Print();
	}
	// MAPA IH SORTIRA !!

	return 0;
}