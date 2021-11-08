#ifndef USER_H
#define USER_H

#include <list>
#include "Message.h"
#include "Post.h"
#include "USocial.h"
#include <iostream>
using namespace std;

class User
{
public:
	unsigned long getId() const;
	string getName() const;
	list<Post*> getPosts() const;
	void addFriend(User*);
	void removeFriend(User*);
	void post(string);
	void post(string, Media*);
	void viewFriendsPosts() const;
	void receiveMessage(User*, Message*);
	void viewReceivedMessages() const;
	
	User();
	~User();

protected:
	USocial* us;
	unsigned long id;
	string name;
	list<unsigned long> friends;
	list<Post*> posts;
	list<Message*> recievedMsgs;
	friend ostream& operator<<(ostream&, const  User&);
	

private:
	static unsigned long user_counter;
};



#endif

