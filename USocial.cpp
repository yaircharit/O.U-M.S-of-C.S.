#include "USocial.h"

unsigned long USocial::user_count = 0;

USocial::USocial() { 
    users = map<unsigned long, User*>();
}
USocial::~USocial() { 
    for (auto pr : users){ delete pr.second; }
 }
User *USocial::registerUser(string username="", bool b=false){
    User *user = new User(username);
    users.insert(pair<unsigned long, User*>(user->getId(), user));
    return user;
}
// User *USocial::registerUser(const char *username=""){
//     string s = username;
//     this->registerUser(s,false);
// }
void USocial::removeUser(User *user) { 
    users.erase(user->getId());
}
User *USocial::getUserById(unsigned long id){
    return users[id];
}