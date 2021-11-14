#pragma once
#include <stdexcept>

using namespace std;

class IllegalMessageException : public std::runtime_error {
public:
	IllegalMessageException(const char *msg = "Illegal Message") : std::runtime_error(msg) { }
	~IllegalMessageException() {}
};
