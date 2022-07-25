#pragma once

#include <string>

class User
{
public:
	User(std::string firstName, std::string lastName, uint16_t age, std::string address);

	std::string getFullName();

private:
	std::string _firstName;
	std::string _lastName;
	uint16_t _age;
	std::string _address;
};
