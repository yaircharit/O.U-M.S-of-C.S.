#ifndef USER_H
#define USER_H

#include <list>
#include "Message.h"
#include "Post.h"
using namespace std;

class User
{
public:
	unsigned long getId() { return id; }
	string getName() { return name; }
	list<Post*> getPosts();
	void addFriend(User*);
	void removeFriend(User*);
	void post(string);
	void post(string, Media*);
	void viewFriendsPosts();
	void receiveMessage(User*, Message*);
	void viewReceivedMessages();
	

protected:
	USocial* us;
	unsigned long id;
	string name;
	list<unsigned long> friends;
	list<Post*> posts;
	list<Message*> recievedMsgs;

	User();
	~User();

private:

};



#endif

