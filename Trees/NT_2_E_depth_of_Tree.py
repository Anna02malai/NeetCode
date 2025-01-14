# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:    
        res = 0
        stk = [[root, 1]]

        while stk:
            node, depth = stk.pop()

            if node:
                res = max(res, depth)
                stk.append([node.left, depth+1])
                stk.append([node.right, depth+1])
            return res

def main():
    root = [1,2,3,null,null,4] 
    res = Solution()
    print(res.maxDepth(root))

if __name__ == "__main__":
    main()