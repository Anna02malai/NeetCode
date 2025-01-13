# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            #reverese the group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp1 = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp1
        return dummy.next

    def getKth(self, curr, k):
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr 

def main():
    head = [1,2,3,4,5]
    k = 3
    res = Solution()
    print(res.getKth(head, k))

if __name__ == "__main__":
    main()