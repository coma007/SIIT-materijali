#include "Person.h"

Person::Person(void)
{
}


Person::~Person(void)
{
}


std::string Person::getName()
{
	return m_name;
}


void Person::setName(std::string name)
{
	m_name = name;
}


int Person::getAge()
{
	return m_age;
}


void Person::setAge(int age)
{
	m_age = age;
}

