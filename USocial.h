#ifndef USOCIAL_H
#define USOCIAL_H

#include <map>
#include "User.h"
class User;
using namespace std;

class USocial
{
public:
	USocial();
	~USocial();
	User * registerUser(string s, bool b);
	// User * registerUser(const char *s);
	void removeUser(User* u);
	User* getUserById(unsigned long id);
private:
	map<unsigned long, User*> users;
	static unsigned long user_count;
};

#endif

