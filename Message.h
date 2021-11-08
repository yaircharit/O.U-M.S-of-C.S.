#ifndef MESSAGE_H
#define MESSAGE_H

#include <string>
using namespace std;

class Message
{
public:
	Message(string txt = "Message") { text = txt; }
	~Message(){}

	string getText() { return text; }
	static unsigned long msg_counter;
private:
	string text;
	
};
//unsigned long Message::msg_counter = 0;

#endif
