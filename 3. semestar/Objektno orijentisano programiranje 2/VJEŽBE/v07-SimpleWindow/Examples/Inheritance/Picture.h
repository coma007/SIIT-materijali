#pragma once

#include <string>

class Picture
{
	std::string m_img;		// private by default
public:
	Picture(void);
	~Picture(void);
	void setPicture(std::string img);
	std::string getPicture();
};

