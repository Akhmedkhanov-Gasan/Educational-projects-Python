class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

head = reverse_linked_list(a)

curr = head
while curr:
    print(curr.val)
    curr = curr.next