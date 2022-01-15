'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
104 Maximum Depth of Binary Tree
'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self,root:TreeNode):
        if not root :
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
