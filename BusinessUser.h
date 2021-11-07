#ifndef BUSINESSUSER_H
#define BUSINESSUSER_H

#include <string>
#include "User.h"
using namespace std;

class BusinessUser : public User
{
public:
	void SendMessage(User*, Message*);

	BusinessUser();
	~BusinessUser();

private:

};



#endif


