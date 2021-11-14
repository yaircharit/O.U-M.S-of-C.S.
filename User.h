#pragma once
#include "NotFriendsException.h"
#include "AlreadyFriendsException.h"
#include "IllegalMessageException.h"
#include <list>
#include <algorithm>
#include "Message.h"
#include "Post.h"
class USocial;

class User
{
public:
	unsigned long getId() const;
	string getName() const;
	list<Post*> getPosts() const;
	void addFriend(User*);
	void removeFriend(User*);
	void post(string text, Media* media = nullptr);
	void viewFriendsPosts() const;
	void receiveMessage(Message*);
	virtual void sendMessage(User*, Message*) const;
	void viewReceivedMessages() const;

	static unsigned long user_counter;
protected:
	USocial* us;
	unsigned long id;
	string name;
	list<unsigned long> friends;
	list<Post*> posts;
	list<Message*> recievedMsgs;
	User(USocial * const net = NULL, string username = "");
	~User();

	friend ostream& operator<<(ostream&, const  User&);
	friend class USocial;

};
