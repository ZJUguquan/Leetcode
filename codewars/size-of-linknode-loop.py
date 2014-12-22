'上周刚用过的 王八算法'
def loop_size(node):
    turtle, rabbit = node.next, node.next.next

    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next

    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count

from itertools import count

def loop_size(node):
    for i in count():
        node.index = i
        try:
            return node.index - node.next.index + 1
        except AttributeError:
            node = node.next

class Node():
    def __init__(self):
        self.next = None


node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1


def loop_size(node):
    init = 0
    head = Node()
    head.next = node
    pointer = {}
    pointer[id(head)] = init
    if node is None or node.next is None:
        return 0
    while head.next is not None:
        init += 1
        if id(head.next) not in pointer:
            pointer[id(head.next)] = init
        else:
            return init - pointer[id(head.next)]
        head = head.next
    return 'not found sry.'

print(loop_size(node1))
# Make a longer chain with a loop of 29
nodes = [Node() for _ in range(50)]
for node, next_node in zip(nodes, nodes[1:]):
    node.next = next_node
nodes[49].next = nodes[21]
print(loop_size(nodes[0]))