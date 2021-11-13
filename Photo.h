#pragma once
#include "Media.h"
class Photo :
	public Media
{
public:
	void display() { cout << "Photo:\t"; }
};

