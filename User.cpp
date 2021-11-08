#include "User.h"

unsigned long User::user_counter = 0;
User::User() {
	id = user_counter++;
	name = "User #"+ to_string(id);
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
void User::addFriend(User* user) {
	friends.push_back(user->id);
}
void User::removeFriend(User* user) {
	friends.remove(user->id);
}
void User::post(string text) {
	posts.push_back(new Post(text));
}
void User::post(string text, Media*media) {
	posts.push_back(new Post(text, media));
}
void User::viewFriendsPosts() const {
	
}
void User::receiveMessage(User*, Message*) {

}
void User::viewReceivedMessages() const {
	for (Message* msg : recievedMsgs) { cout << msg << endl; }
}

ostream& operator<<(ostream& os, const User& user) {
	return os << user.name;
}