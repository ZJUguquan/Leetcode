# coding: utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.previous = None

    def __repr__(self):
        output = '@@\n'
        if self.next is None:
            return 'single: {}'.format(self.val)

        while self.next is not None:
            output += '-->{}'.format( str(self.val))
            self = self.next
        output += '-->{}'.format( str(self.val))
        output += '\n@@'
        return output



class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        if head.next is not None and head.next.next is None:
            pointer = head.next
            pointer.next = head
            head.next = None
            return pointer


        new_head = None
        while head:
            head.next, head, new_head = new_head, head.next, head
        return new_head


s = Solution()
c1 = ListNode('a')
c2 = ListNode('b')
c3 = ListNode('c')
c1.next = c2
c2.next = c3

print s.reverseList(c1)



