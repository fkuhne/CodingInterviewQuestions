#include "Array.h"
#include <iostream>

using namespace std;

// Function to slice the given array
// elements from range (X, Y)
vector<int> slicing(vector<int> v, unsigned X, unsigned Y)
{
	vector<int>::iterator first = v.begin() + X;
	vector<int>::iterator last = v.begin() + X + Y;
	vector<int> w(first, last);
	printVector(w);
	return w;
}

int MaxSubarraySum(vector<int> v)
{
	int size = v.size();
	if (size == 1) return v[0]; // base case

	// Divide and conquer technique!
	int m = size / 2;
	int leftMss = MaxSubarraySum(slicing(v, 0, m));
	int rightMss = MaxSubarraySum(slicing(v, m, size - m));

	int leftSum = INT_MIN, rightSum = INT_MIN, sum = 0;

	// Find the best possible sum in the left half, if any.
	// For the left part, we start at the end (actually, at the
	// middle of the original, unsliced array) and expand to the
	// beggining (more to the left) in order to find the sum with
	// highest value.
	for (int i = m - 1; i >= 0; i--) {
		sum += v[i];
		leftSum = max(sum, leftSum);
	}
	
	sum = 0;
	// Find the best possible sum in the right half, if any
	for (int i = m; i < size; i++) {
		sum += v[i];
		rightSum = max(sum, rightSum);
	}

	int maxForEachPart = max(leftMss, rightMss);
	int maxForBothParts = leftSum + rightSum;
	return max(maxForEachPart, maxForBothParts);
}

// Computes the Maximum Subarray Sum, but the vector
// must contain at least one positive element
int KadaneMSS(vector<int> v)
{
	int ans = 0, sum = 0;
	for (int i : v) {
		sum += i;
		if (sum <= 0) sum = 0;
		ans = max(ans, sum);
	}
	return ans;
}

void printVector(vector<int> v)
{
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << ' ';
	}
	cout << endl;
}
