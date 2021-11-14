#include "Post.h"

ostream &operator<<(ostream &os, const Post &p)
{
	if (p.media != nullptr) //Print media if exists
		p.media->display();

	os << p.text;

	return os;
}