#pragma once

#include <string>

class Person
{
public:
	Person(void);
	~Person(void);
	std::string getName();
	void setName(std::string name);
	int getAge();
	void setAge(int age);
protected:
	std::string m_name;		// can be accessed by derived classes
	int m_age;				// can be accessed by derived classes
};

