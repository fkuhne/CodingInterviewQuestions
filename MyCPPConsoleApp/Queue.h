#pragma once

#include "LinkedList.h"

class queue {
public:
	void enqueue(int value);
	int dequeue();
	bool isEmpty();
	void print();
	void clear();
private:
	node* front = nullptr;
	node* rear = nullptr; /* a pointer to the last node so that a dequeue operation 
						   * can be done on O(1) time. */
};
