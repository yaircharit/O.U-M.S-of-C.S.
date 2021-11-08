#include "USocial.h"

USocial::USocial() { 
    users = map<unsigned long, User*>();
}
USocial::~USocial() { 
    for (auto pr : users){ delete pr.second; }
 }
User *USocial::registerUser(string username, bool b){
    User *user = new User(this,username);
    users.insert(pair<unsigned long, User*>(user->getId(), user));
    return user;
}

void USocial::removeUser(User *user) { 
    users.erase(user->getId());
}
User *USocial::getUserById(unsigned long id){
    return users[id];
}

ostream& operator<<(ostream& os, const USocial& us) {
	for (auto pr : us.users){ os << *pr.second << endl; }
    return os;
}