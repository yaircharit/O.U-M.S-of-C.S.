#ifndef USOCIAL_H
#define USOCIAL_H

#include <map>
#include "User.h"
using namespace std;

class USocial
{
public:
	User* registerUser(string, bool);
	void removeUser(User*);
	User *getUserById(unsigned long);
	friend class User;
private:
	map<unsigned long, User*> users;
};

#endif

