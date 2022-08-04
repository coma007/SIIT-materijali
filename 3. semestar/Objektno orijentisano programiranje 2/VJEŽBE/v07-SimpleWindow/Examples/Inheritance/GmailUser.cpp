#include "GmailUser.h"


GmailUser::GmailUser(void)
{
}


GmailUser::~GmailUser(void)
{
}


std::string GmailUser::getUsername()
{
	return m_username;
}


void GmailUser::setUsername(std::string username)
{
	m_username = username;
}


std::string GmailUser::getPassword()
{
	return m_password;
}


void GmailUser::setPassword(std::string password)
{
	m_password = password;
}


