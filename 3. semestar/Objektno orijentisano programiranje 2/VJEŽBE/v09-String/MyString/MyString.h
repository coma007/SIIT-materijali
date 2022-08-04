#pragma once

#include <iostream>

class MyString
{
private:
	int length;
	char* charBuffer;
public:
	MyString();
	MyString(char* charset);
	MyString(const MyString &string);
	~MyString();
	
	int stringLength();
	char* buffer();
	MyString operator=(const MyString& s);
	MyString operator=(char* charset);
	MyString operator=(char& c);
	char operator[](int index);
	
	friend char* operator+(MyString& s, MyString& other);
	friend char* operator+(MyString& s, char c);
	friend char* operator+(MyString& s, char* c);
	friend char* operator+(char c, MyString& s);
	friend char* operator+(char*, MyString& s);

	friend std::istream& operator>>(std::istream& in, MyString& s);
	friend std::ostream& operator<<(std::ostream& out, MyString s);
};

