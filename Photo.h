#ifndef PHOTO_H
#define PHOTO_H

#include "Media.h"
using namespace std;

class Photo : public Media
{
public:
	void display() { cout << "Photo" << endl; }

private:

};

#endif
