# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        l, r = head, prev

        while r:
            tmp1, tmp2 = l.next, r.next
            l.next = r
            r.next = tmp1
            l, r = tmp1, tmp2

def main():
    head = [2,4,6,8,10]
    res = Solution(head)
    print(res.reorderList(head))

if __name__ == "__main__":
    main()