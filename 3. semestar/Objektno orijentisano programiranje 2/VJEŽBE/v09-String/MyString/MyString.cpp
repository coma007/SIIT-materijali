#include "MyString.h"

#include <cstring>

//-----------------------------------------------------------
// HELPER FUNCTIONS
//-----------------------------------------------------------
void copyString(char* dst, const char* src)
{
	strcpy(dst, src);
	dst[strlen(src)] = '\0';
}

bool compareString(const char* src1, const char* src2)
{
	if (strcmp(src1, src2) == 0)
		return true;
	return false;
}
//-----------------------------------------------------------
//-----------------------------------------------------------


MyString::MyString():length(0), charBuffer(NULL) { }

MyString::MyString(char* charset): length(strlen(charset)), charBuffer(new char[length + 2]) {
	copyString(charBuffer, charset);
}

MyString::MyString(const MyString &s): length(s.length), charBuffer(new char[length + 2]) {
	copyString(this->charBuffer, s.charBuffer);
}

MyString::~MyString() { }

MyString MyString::operator=(const MyString& s) {
	this->length = s.length;
	delete[] this->charBuffer;
	this->charBuffer = new char[length + 1];
	copyString(this->charBuffer, s.charBuffer);
	return *this;
}

MyString MyString::operator=(char* charset) {
	this->length = strlen(charset);
	delete[] this->charBuffer;
	this->charBuffer = new char[length + 1];
	copyString(this->charBuffer, charset);
	return *this;
}

MyString MyString::operator=(char& c) {
	this->length = 1;
	delete[] this->charBuffer;
	this->charBuffer = new char[2];
	this->charBuffer[0] = c;
	this->charBuffer[1] = '\0';
	return *this;
}

char MyString::operator[](int index) {
	if (index < 0 || index >= this->length) {
		exit(-1);
	}
	else {
	return charBuffer[index];
	}
}

int MyString::stringLength() {
	return this->length;
}

char* MyString::buffer() {
	return this->charBuffer;
}


char* operator+(MyString& s, MyString& other) {
	int length = s.length + other.length + 1;
	char* buffer = new char[length];
	strcpy(buffer, s.charBuffer);
	strcat(buffer, other.charBuffer);
	buffer[length] = '\0';
	return buffer;
}

char* operator+(MyString& s, char* c) {
	int length = s.length + strlen(c) + 1;
	char* buffer = new char[length];
	strcpy(buffer, s.charBuffer);
	strcat(buffer, c);
	buffer[length] = '\0';
	return buffer;
}

char* operator+(MyString& s, char c) {
	char* buffer = new char[s.length + 2];
	strcpy(buffer, s.charBuffer);
	buffer[s.length] = c;
	buffer[s.length + 1] = '\0';
	return buffer;
}

char* operator+(char* c, MyString& s) {
	int length = s.length + strlen(c) + 1;
	char* buffer = new char[length];
	strcpy(buffer, c);
	strcat(buffer, s.charBuffer);
	buffer[length] = '\0';
	return buffer;
}

char* operator+(char c, MyString& s) {
	char* buffer = new char[s.length + 2];
	buffer[0] = c;
	for (unsigned int i = 0; i < s.length; i++) {
		buffer[i + 1] = s.charBuffer[i];
	}
	buffer[s.length + 1] = '\0';
	return buffer;
}

std::istream& operator>>(std::istream& in, MyString& s) {
	char* c = new char[256];
	in >> c;
	delete [] s.charBuffer;
	s.charBuffer = new char[strlen(c) + 1];
	copyString(s.charBuffer, c);
	s.length = strlen(c);
	delete[] c;
	return in;
}

std::ostream& operator<<(std::ostream& out, MyString s) {
	out << s.buffer();
	return out;
}