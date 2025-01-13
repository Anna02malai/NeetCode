"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtoCopy = {None: None}
        curr = head

        while curr:
            copy = Node[curr.val]
            oldtoCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldtoCopy[curr]
            copy.next = oldtoCopy[curr.next]
            copy.random = oldtoCopy[curr.random]
            curr = curr.next
        return oldtoCopy[head]

def main():
    head = [[1,null],[2,2],[3,2]]
    res = Solution()
    print(res.copyRandomList(head))

if __name__ == "__main__":
    main()
