
https://oj.leetcode.com/problems/partition-list/

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



p = [0 for i in range(0,11)]
import random
points = []
for i in range(10):
    points.append(ListNode(random.randint(1,10) ) ) # for i in range(10))]
#print(points)
for i in range(0,9):
    points[i].next = points[i+1]

def lophead(head):
    while head is not None:
        yield "old value: " + str(head.val)
        head = head.next

for i in lophead(points[0]):
    print(i)
print('*'*20)
class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head is None or head.next is None:
            return head
        less = ListNode(x-1);
        lessHead = ListNode(x-2); lessHead.next = less
        great = ListNode(x+1)
        greatHead = ListNode(x+2); greatHead.next = great
        while head is not None:
            if head.val < x:
                less.next = head
                less = less.next
                head = head.next
            else:
                great.next = head
                great = great.next
                head = head.next
        less.next = greatHead.next.next

        #case one
        return lessHead.next.next
s = Solution()
m1 = ListNode(2); m2 =ListNode(1); m1.next = m2 ; x = 1
for i in lophead(s.partition(m1, x)):
    print(i)
# for i in lophead(s.partition(points[0], 4)):
    # print(i)

' it seemed get correct answer, but TLE.'


def partition(head, x):
    lh = ListNode(0); rh = ListNode(0)


  ListNode *partition(ListNode *head, int x) {
    ListNode *lh = new ListNode (0), *rh = new ListNode (0);
    ListNode *lt = lh, *rt = rh;
    ListNode *ret = head;
    while(head)
    {
        if(head->val < x)
            lt = lt->next = head;
        else
            rt = rt->next = head;
        head = head->next;
    }
    lt->next = rh->next;
    rt->next = 0;
    ret = lh->next;
    delete lh;
    delete rh;
    return ret;
}




