
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

node* traverseList(node* root)
{
    node* temp = root;
    while (temp->next != nullptr) temp = temp->next;
    return temp;
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
node* head;
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

inline node* insertAtTheBeggining(node* n, int value)
{
    return new node{ value, n };
}

inline void insertAtTheEnd(node* n, int value)
{
    traverseList(n)->next = new node{ value, nullptr };
}

/*
 * position is zero-based.
 */
void insertAtPosition(node* n, int value, int position)
{    
    if (position == 0) n = insertAtTheBeggining(n, value);
    
    node* temp = n;
    while (--position > 0)
    {
        //if (temp->next == nullptr) break;
        temp = temp->next;
    }
    node* newNode = new node{ value, temp->next };
    temp->next = newNode;
}

node* deleteNodeAtTheBeggining(node* n)
{
    node* temp = n;
    n = temp->next;
    delete temp;
    return n;
}

void deleteNodeAtTheEnd(node* n)
{
    node* temp = n;
    while (temp->next != nullptr) temp = temp->next;
    delete temp->next;
    temp->next = nullptr;
}

void deleteNodeAtPosition(node* n, int position)
{
    if (position == 0) {
        n = deleteNodeAtTheBeggining(n);
        return;
    }
 
    node* temp = n;
    while (--position > 0) temp = temp->next;
    node* nthNode = temp->next; // the one we want to delete
    temp->next = nthNode->next; // adjust the link, bypassing the nth node
    delete nthNode;
}

node* getNodeAt(node* n, unsigned position)
{
    node* temp = n;
    while (temp != nullptr && position-- > 0) temp = temp->next;
    return temp;
}

int linkedListSize(node* n)
{
    node* temp = n;
    int size = 0;
    while (n != nullptr) {
        size++;
        n = n->next;
    }
    return size;
}

node* findMergePoint(node* A, node* B)
{
    int sizeOfA = linkedListSize(A);
    int sizeOfB = linkedListSize(B);
    node* list1 = A;
    node* list2 = B;
    if (sizeOfA > sizeOfB) {
        int sizeDiff = sizeOfA - sizeOfB;
        while (sizeDiff-- > 0) list1 = list1->next;
    } else if (sizeOfB > sizeOfA) {
        int sizeDiff = sizeOfB - sizeOfA;
        while (sizeDiff-- > 0) list2 = list2->next;
    }
    while (list1 != nullptr && list2 != nullptr) {
        if (list1 == list2) return list1;
        list1 = list1->next;
        list2 = list2->next;
    }
    return nullptr; /* no merge point */
}
