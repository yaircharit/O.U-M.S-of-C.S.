#ifndef POST_H
#define POST_H

#include "Media.h"
using namespace std;

class Post
{
public:
	Post(string);
	Post(string, Media*);
	~Post();

	string getText() { return text; }
	Media* getMedia() { return media; }

private:
	string text;
	Media* media;
};

#endif
