#include "BusinessUser.h"

void BusinessUser::sendMessage(User*user, Message*msg) const {
	if (user != nullptr)
		user->receiveMessage(msg);
}