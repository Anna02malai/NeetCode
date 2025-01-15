from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []

        while q:
            rightSide = None
            node = q.popleft()
            qlen = len(q)

            for i in range(qlen):
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res

def main():
    root = [1,2,3,4,5,6,7]
    res = Solution()
    print(res.rightSideView(root))

if __name__ == "__main__":
    main()
