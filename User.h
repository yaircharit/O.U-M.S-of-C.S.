#ifndef USER_H
#define USER_H

#include "NotFriendsException.h"
#include <list>
#include <algorithm>
#include "Message.h"
#include "Post.h"
#include <iostream>
class USocial;
#include "USocial.h"

using namespace std;

class User
{
public:
	unsigned long getId() const;
	string getName() const;
	list<Post*> getPosts() const;
	void addFriend(User*);
	void removeFriend(User*);
	void post(string text, Media* media=nullptr);
	void viewFriendsPosts() const;
	void receiveMessage(Message*);
	virtual void sendMessage(User*,Message*) const;
	void viewReceivedMessages() const;

	static unsigned long user_counter;
protected:
	USocial* us;
	unsigned long id;
	string name;
	list<unsigned long> friends;
	list<Post*> posts;
	list<Message*> recievedMsgs;
	User(USocial * const net=NULL, string username="");
	~User();

	friend ostream& operator<<(ostream&, const  User&);
	friend class USocial;

private:
	
};

class BusinessUser : public User
{
public:
	void sendMessage(User*, Message*) const override;

	BusinessUser(USocial * const net=NULL, string username="") :User(net,username) {;}
	~BusinessUser();

private:

};



#endif

