#pragma once
#include <stdexcept>

using namespace std;

class NotFriendsException : public std::runtime_error {
public:
	NotFriendsException(const char *msg= "Users are NOT friends!") : std::runtime_error(msg) { }
	~NotFriendsException() {}
};