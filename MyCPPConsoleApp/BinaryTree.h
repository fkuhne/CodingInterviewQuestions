#pragma once

#include <utility>

struct BinaryTree {
	int value;
	BinaryTree* left = nullptr;
	BinaryTree* right = nullptr;
};

typedef std::pair<int, int> range;

bool isBinarySearchTree(BinaryTree*, const range&);
