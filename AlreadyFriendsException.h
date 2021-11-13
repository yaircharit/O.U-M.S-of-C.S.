#pragma once
#include <stdexcept>

using namespace std;

class AlreadyFriendsException : public std::runtime_error {
public:
	AlreadyFriendsException(const char *msg = "Users are ALREADY friends!") : std::runtime_error(msg) { }
	~AlreadyFriendsException() {}
};
