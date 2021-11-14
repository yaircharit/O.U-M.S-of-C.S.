#include "USocial.h"
#include "User.h"

unsigned long User::user_counter = 0;		//static user counter
User::User(USocial * const net, string username) {
	us = net;
	id = user_counter++;
	name = (username == "") ? "User #" + to_string(id) : username; //default username
	friends = list<unsigned long>();
	posts = list<Post*>();
	recievedMsgs = list<Message*>();
}

User::~User() {
	for (Post* post : posts) { delete post; }
	for (Message* msg : recievedMsgs) { delete msg; }
}

unsigned long User::getId() const { return id; }
string User::getName() const { return name; }
list<Post*> User::getPosts() const { return posts; }
void User::addFriend(User* user) throw (AlreadyFriendsException) {
	if (find(friends.begin(), friends.end(), user->getId()) != friends.end())
		throw AlreadyFriendsException();
	friends.push_back(user->id);
}
void User::removeFriend(User* user) {
	if (user != nullptr)
		friends.remove(user->id);
}

void User::post(string text, Media*media) {
	posts.push_back(new Post(text, media));
}
void User::viewFriendsPosts() const {
	for (auto friend_id : friends) {
		User *user = us->getUserById(friend_id);
		for (auto post : user->posts) {
			cout << *post << endl;
		}
	}
}
void User::receiveMessage(Message*msg) throw(IllegalMessageException) {
	if (msg == nullptr)
		throw IllegalMessageException();
	recievedMsgs.push_back(msg);
}
void User::sendMessage(User*user, Message*msg) const throw (NotFriendsException){
	if (find(friends.begin(), friends.end(), user->getId()) == friends.end())
		throw NotFriendsException();
	user->receiveMessage(msg);
}
void User::viewReceivedMessages() const {
	for (auto msg : recievedMsgs) { cout << *msg << endl; }
}

ostream& operator<<(ostream& os, const User& user) {
	return os << user.name;
}

