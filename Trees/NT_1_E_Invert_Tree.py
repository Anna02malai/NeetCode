# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       
       #Recursiom
        # if not root:
        #     return None
        
        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        #Iteration
        if not root:
            return None
        
        stk = [root]
        while stk:
            node = stk.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        
        return root

def main():
    root = [1,2,3,4,5,6,7]
    res = Solution()
    print(res.invertTree(root))

if __name__ == "__main__":
    main()