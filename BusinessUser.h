#pragma once
#include "User.h"
class User;

class BusinessUser :
	public User
{
public:
	void sendMessage(User*, Message*) const override;

	BusinessUser(USocial * const net = NULL, string username = "") :User(net, username) { ; }
	~BusinessUser() { ; }
};

