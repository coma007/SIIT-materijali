#include "GooglePlusUser.h"


GooglePlusUser::GooglePlusUser(void)
{
}


GooglePlusUser::~GooglePlusUser(void)
{
}


void GooglePlusUser::setProfilePicture(Picture& picture)
{
	m_profilePicture = picture;
}


Picture& GooglePlusUser::getProfilePicture()
{
	return m_profilePicture;
}
