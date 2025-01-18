# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
        
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        self.i = 0

        def dfs():
            if res[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(res[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node
    
        return dfs()

def main():
    root = [1,2,3,null,null,4,5]
    res = Codec()
    print(Codec.serialize(root))

if __name__ == "__main__":
    main()
