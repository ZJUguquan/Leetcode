'Insertion Sort List'

'Sort a linked list using insertion sort.'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or head.next is None:
        	return head
        newHead = ListNode(float('-inf'))
        newHead.next = head
        while head.next is not None:
            prep = head
            post = head.next
            cur_head = newHead
            while cur.val < post.val and cur.next is not None:
                cur = cur.next
            # insertion,
            # insert post   position:  before cur.
                if cur.next.val > next.val:
                    # insert between cur * cur _next
                    prep.next = next.next
                    next.next = cur.next
                    cur.next = next
                    next = prep
                    break
                cur = cur.next
        	# if head.val < sorted_head.val:
        	# 	head.next = sorted_head
        	# 	sorted_head.next = head
        	# else:
        	# 	temp = sorted_head
        	# 	while (temp.next is not None ) and temp.val <= head.val:
        	# 		temp = temp.next
        	# 	tail = temp.next
        	# 	temp.next = head
        	# 	head.next = tail
        	head = next

        result = newHead.next
        return result


l1 = ListNode(1)
l2 = ListNode(2); l1.next = l2
s = Solution()
s.insertionSortList(l1)

print(l1.val)
print(l1.next)
print()
while l1.next is not None:
	l1 = l1.next
	print(l1.next)


'it seems others guys also got TLE using Python. it relieved me...'
'reference '


class Solution:
# @param head, a ListNode
# @return a ListNode
def insertionSortList(self, head):
    linkHead = ListNode(0)
    linkHead.next = head
    sortedEnd = linkHead.next
    if sortedEnd == None:
        return head
    innerPointer = linkHead.next  #declare innerPointer here

    while sortedEnd.next != None:
        pointer = sortedEnd.next
        sortedEnd.next = pointer.next

        # reset innerPointer only when pointer is needed to be inserted before innerPointer
        if innerPointer.val > pointer.val: # bigger than bigger, just append.
            innerPointer = linkHead

        while innerPointer != sortedEnd and innerPointer.next.val < pointer.val:
            innerPointer = innerPointer.next

        pointer.next = innerPointer.next
        innerPointer.next = pointer

        if innerPointer == sortedEnd:
            sortedEnd = pointer

    return linkHead.next