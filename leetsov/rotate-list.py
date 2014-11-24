"https://oj.leetcode.com/problems/rotate-list/"


"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next=l2;l2.next=l3
l3.next =l4; l4.next = l5
def loopnode(head):
    while head is not None:
        yield head.val
        head = head.next

for x in loopnode(l1):
    print(x)
print('*'*40)
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        def getLength(head):
            Nlen = 0
            while head is not None:
                Nlen += 1
                head = head.next
            return Nlen

        N = getLength(head)
        if N== 0 or head.next is None:
            return head
        N = N - k % N # position to break.
        p = head; count = 0
        while (p is not None and count < N - 1):
            p = p.next
            count += 1 # p.next is newHead

        temp = p.next
        q = ListNode(0)
        q.next = temp
        p.next = None

        if temp is not None:
            while(temp.next is not None):
                temp = temp.next
        #print(temp==None)
        temp.next = head
        return q


s = Solution()
s.rotateRight(l1, 2)
for x in loopnode(l4):
    print(x)

"""

    ListNode t=p.next,q;
    p.next=null;
    q=t;
    while(t.next!=null) t=t.next;
    t.next=head;
    return q;
}
"""