#pragma once

#include <string>
#include "GmailUser.h"
#include "Picture.h"

class GooglePlusUser : public GmailUser
{
private:
	Picture m_profilePicture;
public:
	GooglePlusUser(void);
	~GooglePlusUser(void);
	void setProfilePicture(Picture& picture);
	Picture& getProfilePicture();
};

