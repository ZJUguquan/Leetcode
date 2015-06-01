# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
l4 = ListNode(4)
l5 = ListNode(5)
l3.next = l4
l4.next = l5


def loopnode(head):
    while head is not None:
        yield head.val
        head = head.next

for value in loopnode(l1):
    print(value)


class Solution:
    # @return a ListNode

    def getLength(self, head):
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length

    def removeNthFromEnd(self, head, n):
        N = self.getLength(head)
        if head is None or n == 0:
            return head
        if n > N:
            return head
        if head.next is None:
            return None
        if n == N:
            return head.next

        to_delete_number = N - n + 1
        pos = 0
        result = ListNode(0)
        result.next = head
        while head is not None:
            pos += 1
            if pos == to_delete_number - 1:
                previous = head
                previous.next = head.next.next
                break
            head = head.next
        return result.next

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
s.removeNthFromEnd(l1, 1)

print('*' * 40)
for value in loopnode(l1):
    print(value)
