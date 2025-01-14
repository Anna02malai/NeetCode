# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs():
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)        
            self.res = max(self.res, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.res

def main():
    root = [1,null,2,3,4,5]
    res = Solution()
    print(res.diameterOfBinaryTree(root))

if __name__ == "__main__":
    main()
