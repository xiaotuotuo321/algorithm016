# -*- coding: utf-8 -*-
"""
从前序和中序遍历序列构造二叉树

解体思路
从前序遍历中可以得到根节点：根左右；再从中序遍历左根右，确定左右子树
每次递归都要确保前序列表和中序列表的元素个数是相同的
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        loc = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: loc + 1], inorder[:loc])
        root.right = self.buildTree(preorder[loc + 1:], inorder[loc + 1:])

        return root
