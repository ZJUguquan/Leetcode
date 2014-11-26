"""Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}."""


# Definition for singly-linked list.
'https://oj.leetcode.com/problems/reorder-list/'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None or head.next.next is None: return head
        house = {} # save position:Listnode
        beginning = 0
        newHead = ListNode(0); newHead.next = head;
        house[beginning] = newHead
        while head is not None:
            beginning += 1
            house[beginning] = head
            head = head.next

        # at leat length  == 3
class Solution:
    def reorderList(self, head):
        if head is None or head.next is None or head.next.next is None: return head
        h = self.reorderList(head, head, head)

    def reorderList(prev, slow, faster):
        if faster is None or faster.next is None:
            if faster is not None:
                reverse = slow. next
                slow.next = None
                return reverse
        prev.next = None
        return slow
'''

    if(faster == null || faster.next == null) {
        if(faster != null) {
            ListNode reverse = slow.next;
            slow.next = null;
            return reverse;
        }
        prev.next = null;
        return slow;
    }
    ListNode retNode = reorderList(slow, slow.next, faster.next.next);
    // concanate
    ListNode temp = retNode.next;
    retNode.next = slow.next;
    slow.next = retNode;
    return temp;
}
'''