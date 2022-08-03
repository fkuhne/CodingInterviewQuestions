#pragma once

#include "LinkedList.h"
#include <vector>

class stack {
public:
	void push(int value);
	int pop();
	bool isEmpty();
private:
	int top = 0;
	node* lifo = nullptr;
};

int evaluatePostfix(std::vector<char>);
