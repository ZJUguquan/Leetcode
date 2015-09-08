class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):

        output = str(self.data)
        while self.next:
            self = self.next
            output += '->' + str(self.data) + ''
        output += '->nil'

        return output

    def __repr__(self):
        output = str(self.data)
        while self.next:
            self = self.next
            output += '->' + str(self.data) + ''
        output += '->nil'

        return output


def insert_nth(head, index, data):
    res = []
    if head is None:
        return Node(data)
    res.append(head)
    if index == 0:
        node = Node(data)
        node.next = head
        res.insert(0, node)
    else:

        toinsert = Node(data)
        while head.next is not None:
            head = head.next
            res.append(head)
        if index > len(res):
            raise Exception('Invalid index value')

        elif len(res) == index:
            res[-1].next = toinsert

        else:
            temp = res[index - 1].next
            res[index - 1].next = toinsert
            toinsert.next = temp

    return res[0]


def build_123():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    return head

a = build_123()
print("123")
print(str(a))

insert_nth(a, 3, 23)
print(a)


-- length and count


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    if not node:
        return 0
    leng = 1
    while node.next:
        leng += 1
        node = node.next
    return leng


def count(node, data):
    if not node:
        return 0

    leng = 0
    while node.next:
        if node.data == data:
            leng += 1
        node = node.next
    if node.data == data:
        leng += 1
    return leng


-- get N th


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    if index < 0:
        raise Exception("INvalid index value should throw error")
    pos = 0
    if pos == index:
        if node is None:
            raise Exception("INvalid index value should throw error")
        return node
    while pos < index:
        node = node.next
        pos += 1
    if node is None:
        raise Exception("INvalid index value should throw error")
    return node
