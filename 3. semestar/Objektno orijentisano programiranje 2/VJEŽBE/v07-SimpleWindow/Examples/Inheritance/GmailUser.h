#pragma once

#include <string>
#include "Person.h"

class GmailUser : public Person
{
public:
	GmailUser(void);
	~GmailUser(void);
	std::string getUsername();
	void setUsername(std::string username);
	std::string getPassword();
	void setPassword(std::string password);
protected:
	std::string m_username;		// can be accessed by derived classes
	std::string m_password;		// can be accessed by derived classes
};

