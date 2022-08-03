// MyCPPConsoleApp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <cassert>

#include "User.h"
#include "BinarySearch.h"
#include "LinkedList.h"
#include "BinaryTree.h"
#include "Array.h"
#include "Stack.h"
#include "Queue.h"

using namespace std;

int main()
{
    cout << "Hello World!\n";

    User user1("Felipe", "Kuhne", 43, "Av. Bagé");
    cout << user1.getFullName() << endl << endl;

    /*
     * BINARY SEARCH
     */
#if 0
    vector<int> v{ 2,4,10,10,10,18,20 };
    int target = 10;
    int r = binarySearch(v, target);
    cout << r << endl << endl;

    int first = binarySearch2(v, target, true);
    if (first == -1) cout << target << " not found" << endl;
    else {
        int last = binarySearch2(v, target, false);
        cout << last - first + 1 << endl << endl;
        cout << "first is " << first << ", last is " << last << endl;
    }
#endif

    /*
     * LINKED LISTS
     */
#if 0
    node* n = createRandomLinkedList();
    printList(n);
    //printReversedList(n);
    //recursiveReverseList(n);
    //printList(n);

    node* n2 = traverseList(n);
    cout << "the last value of n is " << n2->value << endl;

    n = insertAtTheBeggining(n, 69);
    printList(n);

    insertAtTheEnd(n, 666);
    printList(n);

    insertAtPosition(n, 111, 3);
    printList(n);

    n = deleteNodeAtTheBeggining(n);

    //deleteNodeAtPosition(n, 0);
    //printList(n);

    //deleteNodeAtTheEnd(n);
    //printList(n);

    node* listA = new node{ 1, new node{2, new node{3, new node{4, new node{5, nullptr}}}} };
    node* mergePoint = getNodeAt(listA, 3);
    node* listB = new node{ 9, new node{9, new node{ 9, new node{9, new node{9, mergePoint}}}}};
    node* merge = findMergePoint(listA, listB);
    printList(merge);

#endif

    /*
     * BINARY TREES
     */
#if 0
    BinaryTree t{ 10,               /*root*/
        new BinaryTree{5,           /*left*/
            new BinaryTree{4,       /*left*/
                new BinaryTree{1}   /*left*/
            },
            new BinaryTree{7,       /*right*/
                nullptr,            /*left*/
                new BinaryTree{8}   /*right*/
                }
            },
        new BinaryTree{16}          /*right*/
    };

    cout << "t is a BST? " << isBinarySearchTree(&t, range{ INT_MIN, INT_MAX });
#endif


    /*
     * ARRAYS 
     */
#if 0
    vector<int> v{ 3,-2,5,-1 };
    int mss = MaxSubarraySum(v);
    cout << "mss = " << mss << endl;
    cout << "kmss = " << KadaneMSS(v) << endl;
#endif

    /*
     * STACKS
     */
#if 0
    vector<char> exp{ '2', '3', '*', '5', '4', '*', '+', '9', '-'};
    cout << evaluatePostfix(exp);
#endif

    /* 
     * QUEUES
     */
    queue q;
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);
    q.print();
    for (int i = 0; i < 3; i++) cout << "dequeued val is " << q.dequeue() << endl;
    q.enqueue(7);
    q.print();
    q.clear();
    q.print();
    cout << "q is empty? " << q.isEmpty() << endl;

}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
