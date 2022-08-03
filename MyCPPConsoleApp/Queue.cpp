#include "Queue.h"
#include <climits>

/*
 * Add a node at the end of the fifo, which is the rear node.
 * Keep track of the rear pointer so that insertions can be
 * done in O(1) time.
 */
void queue::enqueue(int value)
{
	node* temp = new node{ value, nullptr };
	if (this->front == nullptr && this->rear == nullptr) {
		// we are in the head of the list.
		this->front = temp;
		this->rear = temp;
	}
	else {
		this->rear->next = temp; // points next to the new element
		this->rear = temp; // updates the address of rear
	}
}

/*
 * Remove the first item of the fifo, which is in the front. 
 */
int queue::dequeue()
{
	if (this->isEmpty()) return -INT_MAX;
	int value = this->front->value;
	this->front = deleteNodeAtTheBeggining(this->front); // O(1) operation
	if (this->isEmpty()) this->rear = nullptr;
	return value;
}

bool queue::isEmpty()
{
	return (this->front == nullptr);
}

void queue::print()
{
	printList(this->front);
}

void queue::clear()
{
	while (this->front != nullptr) this->front = deleteNodeAtTheBeggining(this->front);
	this->rear = nullptr;
}
