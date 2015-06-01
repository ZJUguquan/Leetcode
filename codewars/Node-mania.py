

class Node(object):

    def __init__(self):
        self.data = None  # contains the data
        self.next = None  # contains the reference to the next node


class LinkedList(object):

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node()  # create a new node
        new_node.data = data
        new_node.next = self.head  # link the new node to the 'previous' node.
        self.head = new_node  # set the current node to the new one.

    # A method that appends to the tail instead of the head
    def append(self, data):
        new_node = Node()
        new_node.data = data
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    def to_list(self):
        output = []
        pointer = self.head
        if pointer is not None:
            output.append(pointer.data)
        while pointer.next:
            pointer = pointer.next
            output.append(pointer.data)
        return output

    def __repr__(self):
        output = ''
        c = 0
        if self.head:
            output += '>>{data}, {n}'.format(data=self.head.data, n=c)
        while self.head.next:
            self.head = self.head.next
            c += 1
            output += '>>{data}, {n}'.format(data=self.head.data, n=c)
        return output

# linked_list.head
def search_k_from_end(linked_list, k):
    output = []
    pointer = linked_list.head
    if pointer is not None:
        output.append(pointer.data)
    while pointer.next:
        pointer = pointer.next
        output.append(pointer.data)
    lens = len(output)
    if k > lens or k < 0:
        return None
    return output[-k]


class Test(object):
    def assert_equals(self, left, right):
        if left == right:
            print left, 'done'
        else:
            print 'something happend, be careful!'
test = Test()



class Node(object):

    def __init__(self):
        self.data = None  # contains the data
        self.next = None  # contains the reference to the next node


class LinkedList(object):

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node()  # create a new node
        new_node.data = data
        new_node.next = self.head  # link the new node to the 'previous' node.
        self.head = new_node  # set the current node to the new one.

    # A method that appends to the tail instead of the head
    def append(self, data):
        new_node = Node()
        new_node.data = data
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    def to_list(self):
        output = []
        pointer = self.head
        if pointer is not None:
            output.append(pointer.data)
        while pointer.next:
            pointer = pointer.next
            output.append(pointer.data)
        return output

    def __repr__(self):
        output = ''
        c = 0
        if self.head:
            output += '>>{data}, {n}'.format(data=self.head.data, n=c)
        while self.head.next:
            self.head = self.head.next
            c += 1
            output += '>>{data}, {n}'.format(data=self.head.data, n=c)
        return output


def search_k_from_end(linked_list, k):
    output = linked_list.to_list()
    print output, len(output)
    return  output[-k]


ll = LinkedList()
ll.add(1)
ll.append(2)
ll.append(3)
ll.append(4)

print search_k_from_end(ll, 1)

print search_k_from_end(ll, 2)
print search_k_from_end(ll, 3)
print search_k_from_end(ll, 4)

# the list looks like this
# 1 -> 2 -> 3 -> 4



# Test.assert_equals(search_k_from_end(ll, 1), 4)
# Test.assert_equals(search_k_from_end(ll, 2), 3)
# Test.assert_equals(search_k_from_end(ll, 3), 2)
# Test.assert_equals(search_k_from_end(ll, 4), 1)
