// MyCPPConsoleApp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>

#include "User.h"
#include "BinarySearch.h"
#include "LinkedList.h"

using namespace std;

int main()
{
    cout << "Hello World!\n";

    User user1("Felipe", "Kuhne", 43, "Av. Bagé");

    cout << user1.getFullName() << endl << endl;

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

    node *n = createRandomLinkedList();
    printList(n);
    printReversedList(n);
    recursiveReverseList(n);
    printList(head);
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
