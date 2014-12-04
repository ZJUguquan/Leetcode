#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'STEVE'

"""documents:
   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
# #         self.next = None

# class Solution:
#     # @return a ListNode
#     def removeNthFromEnd(self, head, n):
#     	assert n > 0
#     	# create a dummy node > before head.
#     	dummy = ListNode(-1)
#         dummy.next = head
#         slow, fast = dummy, dummy
#     	pos = -1
#     	# main loop
#     	for i in range(n):
#     		fast = fast.next
#     		assert fast
#     	while fast.next:
#     		pos += 1


# class Solution:
#     # @return a ListNode
#     '''
#     n = 5
#     (-1)->1->2->3->4->5

#     i    =    0->1->2->3->4->5
#     fast = (-1)->1->2->3->4->5

#     fast = 5
#     slow = (-1)

#     slow.next = head.next = 2
#     '''
#     def removeNthFromEnd(self, head, n):
#         assert n > 0
#         dummy = ListNode(-1)
#         dummy.next = head
#         slow, fast = dummy, dummy
#         for i in range(n):
#             fast = fast.next
#             assert fast
#         while fast.next:
#             fast = fast.next
#             slow = slow.next
#         slow.next = slow.next.next
#         return dummy.next

A = [1,2,3]
A = []; B=[1]
# B = [5,6,4]
C = A+B

print(sorted(C))