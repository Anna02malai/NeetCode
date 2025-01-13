# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = head

        for i in range(n):
            first = first.next
        
        second = dummy

        while first:
            second = second.next
            first = first.next
        
        second.next = second.next.next
    
        return dummy.next

def main():
    head = [1,2,3,4]
    n = 2
    res = Solution()
    print(res.removeNthFromEnd(head, n))

if __name__ == "__main__":
    main()
