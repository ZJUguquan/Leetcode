__author__ = 'STEVE'
__tag__ = "LeetCode"
__status__ == "Accepted"



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

m1 = ListNode('1')
m2 = ListNode('2')
m3 = ListNode('3')
m1.next = m2
m2.next = m3
m3.next = m1

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None or head.next == None:
        	return False
        slow = head
        fast = head
        counter = 0
        while fast is not None:
        	counter += 1
        	if (counter % 2) == 0:
        		slow = slow.next
        	if fast.next == slow:
        		return True
        	fast = fast.next
        return False

        # detect_list =[]
        # detect_list.append(head)
        # detect_list.append(head.next)
        # pos = head.next
        # while pos.next != None:
        # 	if pos.next in detect_list:
        # 		# form cycle
        # 		return True
        # 	pos = pos.next
        # return False

print m1.next.val

s = Solution()
print s.hasCycle(m1)
