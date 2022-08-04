#include "Picture.h"

using namespace std;

Picture::Picture(void)
{
}


Picture::~Picture(void)
{
}


void Picture::setPicture(std::string img)
{
	m_img = img;
}


std::string Picture::getPicture()
{
	return m_img;
}
