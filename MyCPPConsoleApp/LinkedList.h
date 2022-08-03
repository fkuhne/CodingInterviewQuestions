#pragma once

struct node {
    int value;
    node* next;
};

void reverseLinkedList();
node* createRandomLinkedList();
node* traverseList(node*);
void printList(node*);
node* reverseList(node*);
void printReversedList(node*);
void recursiveReverseList(node*);

node* insertAtTheBeggining(node*, int);
void insertAtTheEnd(node*, int);
void insertAtPosition(node*, int, int);

node* deleteNodeAtTheBeggining(node*);
void deleteNodeAtTheEnd(node*);
void deleteNodeAtPosition(node*, int);

node* getNodeAt(node*, unsigned);
int linkedListSize(node*);
node* findMergePoint(node*, node*);