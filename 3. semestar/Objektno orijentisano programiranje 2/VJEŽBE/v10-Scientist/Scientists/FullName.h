#pragma once
#include <string>

class FullName
{
	std::string name;
	std::string surname;
public:
	FullName(std::string n, std::string s);
	std::string getName() const;
	std::string getSurname() const;
	bool operator==(const FullName& rhs);
};
