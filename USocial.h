#ifndef USOCIAL_H
#define USOCIAL_H

#include <map>
#include "User.h"
using namespace std;

class USocial
{
public:
	USocial() { ; }
	~USocial() { ; }
	User * registerUser(string s, bool b) { return nullptr; }
	void removeUser(User* u) { ; }
	User* getUserById(unsigned long id) { return nullptr; }
private:
	map<unsigned long, User*> users;
};

#endif

