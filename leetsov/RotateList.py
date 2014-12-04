#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Stevey"
__project__ = "Leetcode"
"Problems: RotateList"


"give 1-2-3-4-5-None"
" k = 2 ,  rotate to the right"
"return "


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l = [0,0,0,0,0]
l[0] = ListNode(0)
for i in range(1,5):
    l[i] = ListNode(i)
    l[i-1].next = l[i]

print l

print l[2].next.val


def rotate_a_list(aList, k):
    if k < len(aList):
        return aList[-k:] + aList[:-k]

aList = [1,2,3,4,5]
print rotate_a_list(aList, 2)


def rotate_a_linked_list(l, k):
    if l == None:
        return None
    if l.next == None :
        return l
    Nodes = [].append(l)
    while l.next :
        Nodes.append(l.next)
        l = l.next

    n = len(Nodes)
    k = k % n
    Nodes[-1].next = Nodes[0]
    Nodes[n-k-1].next = None
    return Nodes[n-k]


print type({1,2})

"****************************************************************************"



"尝试失败  看discuss 改变java code"



# public ListNode rotateRight(ListNode head, int n) {
#     if (head == null || head.next == null || n == 0) {
#          return head;
#     }
#     ListNode fast = head;
#     ListNode slow = head;
#     ListNode newHead;
#     for (int i = 0; i < n; i++) {
#         if (fast.next == null) {
#             fast = head;
#         } else {
#             fast = fast.next;
#         }
#     }
#     while (fast.next != null) {
#         fast = fast.next;
#         slow = slow.next;
#     }
#     fast.next = head;
#     newHead = slow.next;
#     slow.next = null;
#     return newHead;
# }