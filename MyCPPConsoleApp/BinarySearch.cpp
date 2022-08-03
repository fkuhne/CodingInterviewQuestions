
#include "BinarySearch.h"

using namespace std;
/**
Binary search for the first occurence of some target value
*/
int binarySearch(vector<int> v, int target)
{
    int low = 0, high = v.size() - 1;
    while (low <= high)
    {
        int middle = (low + high) / 2;
        if (target == v.at(middle)) return middle;
        if (target < v.at(middle))  high = middle - 1;
        else  low = middle + 1;
    }
    return -1;
}

int binarySearch2(vector<int> v, int target, bool searchFirst)
{
    int low = 0, high = v.size() - 1, result = -1;
    while (low <= high)
    {
        int middle = (low + high) / 2;
        if (target == v.at(middle)) {
            result = middle;
            if (searchFirst) high = middle - 1; // Go on searching towards left
            else low = middle + 1; // Go on searching towards right
        }
        else if (target < v.at(middle)) high = middle - 1;
        else low = middle + 1;
    }
    return result;
}
