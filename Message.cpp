#include "Message.h"

ostream& operator<<(ostream& os, const Message& msg) {
	return os << msg.text;
}
