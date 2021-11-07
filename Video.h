#ifndef VIDEO_H
#define VIDEO_H

#include "Media.h"
using namespace std;

class Video : public Media
{
public:
	void display() { cout << "Video" << endl; }

private:

};

#endif
