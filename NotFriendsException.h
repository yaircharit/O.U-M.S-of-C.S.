#ifndef NOT_FRIENDS_EXCEPTION_H
#define NOT_FRIENDS_EXCEPTION_H

#include <stdexcept>

class NotFriendsException : public std::runtime_error {
private:
    const char *_msg = "Users are NOT friends!";
public:
    NotFriendsException() : std::runtime_error(_msg) {;}
    ~NotFriendsException(){}

    const char* what() const throw(){
        return _msg;
    }
};

#endif