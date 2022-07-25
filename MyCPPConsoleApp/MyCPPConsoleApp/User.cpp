#include "User.h"

using namespace std;

User::User(string firstName, string lastName, uint16_t age, string address)
	: _firstName(firstName), _lastName(lastName), _age(age), _address(address)
{
}

string User::getFullName() {
	return _firstName + " " + _lastName;
}
