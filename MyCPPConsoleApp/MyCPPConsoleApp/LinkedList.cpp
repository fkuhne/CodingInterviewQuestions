
#include "LinkedList.h"
#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>

using namespace std;

void reverseLinkedList()
{
    node list{ 2, new node{4, new node{6, new node{5, nullptr}}} };
    node* t = &list;

    while (t != nullptr)
    {
        cout << t->value << " " << flush;
        t = t->next;
    }
}

node* createRandomLinkedList()
{
    srand(time(0));
    int size = rand() % 10 + 1;
    node* head = new node{ rand() % 100, nullptr };
    if (size == 1) return head;
    node* cur = head;
    while (--size > 0)
    {
        cur->next = new node{ rand() % 100, nullptr };
        cur = cur->next;
    }
    return head;
}

void printList(node* n)
{
    if (n == nullptr) {
        cout << endl;
        return;
    }
    cout << n->value << " " << flush;
    printList(n->next);
}

node* reverseList(node* n)
{
    node* cur = n;
    node* prev = nullptr;
    node* next;
    while (cur != nullptr) {
        next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
    }
    n = prev;
    return n;
}

void printReversedList(node* n)
{
    if (n == nullptr) {
        cout << endl;
        return;
    }
    printReversedList(n->next);
    cout << n->value << " " << flush;
}

void recursiveReverseList(node* n)
{
    if (n->next == nullptr) {
        head = n;
        return;
    }
    recursiveReverseList(n->next);
    node* q = n->next;
    q->next = n;
    n->next = nullptr;
}

