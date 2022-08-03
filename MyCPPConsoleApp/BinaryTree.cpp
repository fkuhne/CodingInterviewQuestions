#include "BinaryTree.h"

bool isBinarySearchTree(BinaryTree* root, const range& allowedRange)
{
	// base cases
	if (root == nullptr) return true;

	if (root->value >= allowedRange.first && root->value < allowedRange.second /*if the node value is within the allowed range*/
		&& isBinarySearchTree(root->left, range{ allowedRange.first, root->value })
		&& isBinarySearchTree(root->right, range{ root->value, allowedRange.second }))
		return true;

	return false;
}
