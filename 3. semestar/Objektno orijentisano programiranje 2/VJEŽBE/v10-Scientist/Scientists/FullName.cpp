#include "FullName.h"

/*
@TODO: Complete the FullName class definition:
- add implementation for constructor with parameters
- add implementation for operator ==
- add implementation for get methods
*/

FullName::FullName(std::string n, std::string s) : name(n), surname(s) {};

std::string FullName::getName() const {
	return name;
}

std::string FullName::getSurname() const {
	return surname;
}

bool FullName::operator==(const FullName& rhs) {
	return name == rhs.getName() && surname == rhs.getSurname();
}
