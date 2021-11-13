#pragma once

#include <string>
using namespace std;
class Message
{
public:
	Message(string txt = "Message") { text = txt; }
	~Message() {}

	string getText() { return text; }
	friend ostream& operator<<(ostream& os, const Message&);
private:
	string text;

};

