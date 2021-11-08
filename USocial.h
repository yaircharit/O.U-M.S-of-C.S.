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
	User * registerUser(string username="", bool b=false);
	// User * registerUser(string s);
	void removeUser(User* u);
	User* getUserById(unsigned long id);
	
private:
	map<unsigned long, User*> users;
	friend ostream& operator<<(ostream&, const  USocial&);
};

#endif

