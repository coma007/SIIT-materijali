#pragma once

#include "FullName.h"

class Scientist
{
	FullName scientist;
	int id;

public:
	Scientist(FullName name, int i);
	bool operator==(const Scientist& rhs);
	bool operator<(const Scientist rhs);
	FullName getFullName() const;
	int getId() const;
};

