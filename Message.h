#ifndef MESSAGE_H
#define MESSAGE_H

#include <string>
using namespace std;

class Message
{
public:
	Message();
	~Message();

	string getText() { return text; }
private:
	string text;
};


#endif
