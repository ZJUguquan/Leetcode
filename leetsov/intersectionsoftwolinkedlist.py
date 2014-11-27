'intersection-of-two-linked-lists'

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def nextval(self):
		while self is not None:
			yield self.val
			self = self.next

a1 = ListNode(1);a2 = ListNode(2)
a1.next = a2
a3 = ListNode(3); a4 = ListNode(4)
a2.next = a3
a3.next = a4
a5 = ListNode(5)
a4.next = a5

'traver a1'
for val in a1.nextval():
	print(val)

b1 = ListNode(10); b2= ListNode(20); b3= ListNode(30)
b3.next = a3



class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
        	return None
        pointerA = ListNode(0); pointerA.next = headA
        pointerB = ListNode(0); pointerB.next = headB
        res = []
        while pointerA.next is not None and pointerB.next is not None:
        	if pointerA == pointerB:
        		print('found begining!')

        	and pointerA != pointerB.next and pointerB != pointerA.next:
        		pointerA = pointerA.next
        		pointerB = pointerB.next

        print('PA value', pointerA.val, 'PB value', pointerB.val)
        # if headA == headB:
        # 	res.append(headB)
        # 	pointer

s = Solution()
print('start solution....' )
s.getIntersectionNode(a1, b1)