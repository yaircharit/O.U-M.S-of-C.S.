#pragma once
#include "Video.h"
#include "Audio.h"
#include "Photo.h"

using namespace std;

class Post
{
public:
	Post(string txt, Media* m = nullptr) : text(txt), media(m) {}
	~Post() { delete media; }

	string getText() { return text; }
	Media* getMedia() { return media; }
	friend ostream& operator<<(ostream&, const Post&);

private:
	string text;
	Media* media;
};

