from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        #DFS:
        # def dfs(node, maxVal):
        #     if not node:
        #         return 0
            
        #     res = 1 if node.val >= maxVal else 0
        #     maxVal = max(node.val, maxVal)
        #     res += dfs(node.left, maxVal)
        #     res += dfs(node.right, maxVal)
        # return dfs(root, root.val)

        #BFS:
        q = deque([root, -float("inf")])
        res = 0

        while q:
            node, maxval = q.popleft()
            if node.val >= maxval:
                res += 1

            if node.left:
                q.append([node.left, max(maxval, node.val)]) 
            if node.right:
                q.append([node.right, max(maxval, node.val)])
        
        return res

def main():
    root = [2,1,1,3,null,1,5]
    res = Solution()
    print(res.goodNodes(root))

if __name__ == "__main__":
    main()
