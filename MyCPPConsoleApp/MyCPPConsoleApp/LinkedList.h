#pragma once

struct node {
    int value;
    node* next;
};

struct node* head;

void reverseLinkedList();
node* createRandomLinkedList();
void printList(node*);
node* reverseList(node*);
void printReversedList(node*);
void recursiveReverseList(node* n);

