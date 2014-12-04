# -*- coding: utf-8 -*-

# __author__ = 'STEVE'
# __tag__ = "LeetCode"
__status__ == "Accepted by others"

"10-29"
"Add Two Numbers"
"Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)"
"Output: 7 -> 0 -> 8"

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
m1 = ListNode(6)
m2 = ListNode(7)
m3 = ListNode(9)
l1.next = l2
l2.next = l3
m1.next = m2
m2.next = m3
" 程序出了问题把电脑跑重启了。 > < "
# def intToLinklist(x):
# 		if x == None:
# 			return None
# 		s = str(x)
# 		if len(s) == 1:
# 			return ListNode(x)
# 		if len(s) == 2:
# 			m = ListNode(int(s[0]))
# 			n = ListNode(int(s[1]))
# 			n = m.next
# 			return m

# 		i = 0
# 		nodes = []
# 		while i <= len(s) - 1:
# 			temp_node = ListNode(int(s[i]))
# 			nodes.append(temp_node)
# 		for i in range(0, len(nodes) - 1):
# 			m = nodes[i]
# 			n = nodes[i+1]
# 			n = m.next
# 		return nodes[0]

# print intToLinklist(321)
# def addTwoNumbers(l1, l2):
#     s1, s2 = "", ""
#     if l1 != None:
#     	s1 += str(l1.val)
#     	while l1.next :
#     		s1 += str(l1.next.val)
#     		l1 = l1.next
#     if l2 != None:
#     	s2 += str(l2.val)
#         while l2.next:
#         	s2 += str(l2.next.val)
#         	l2 = l2.next
#     if s1 == "" and s2 == "":
#     	return None
#     if s1 == "" and s2 != "":
#     	return intToLinklist(int(s2))
# 	if s2 == "" and s1 != "":
# 		return intToLinklist(int(s1))
#     return intToLinklist(int(s1) + int (s2))


#     return s1 , "\t", s2

# print 1
# print addTwoNumbers(l1, m1)
# print 3


"reference"
def addTwoNumbers(l1, l2):
	c1, c2 = l1, l2
	sentinel = ListNode(0)
	d = sentinel
	sum = 0
	while (c1 != None or c2 != None):
		sum /= 10
		if c1 != None:
			sum += c1.val
			c1 = c1.next
		if c2 != None:
			sum += c2.val
			c2 = c2.next
		d.next = ListNode( sum % 10)
		d = d.next
	if (sum / 10 == 1):
		d.next = ListNode(1)
	return sentinel.next

print addTwoNumbers(l1,m1)
"""
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode c1 = l1;
        ListNode c2 = l2;
        ListNode sentinel = new ListNode(0);
        ListNode d = sentinel;
        int sum = 0;
        while (c1 != null || c2 != null) {
            sum /= 10;
            if (c1 != null) {
                sum += c1.val;
                c1 = c1.next;
            }
            if (c2 != null) {
                sum += c2.val;
                c2 = c2.next;
            }
            d.next = new ListNode(sum % 10);
            d = d.next;
        }
        if (sum / 10 == 1)
            d.next = new ListNode(1);
        return sentinel.next;
    }
}
"""