class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def create_node(val):
    newNode = Node()
    newNode.val = val
    return newNode


node1 = create_node(2)
node2 = create_node(3)
node3 = create_node(4)

node1.next = node2
node2.next = node3


def print_linked_list(head):
    if head is None:
        return
    print(head.val)
    print_linked_list(head.next)


def print_linked_list_in_reverse(head):
    if head is None:
        return
    currentHead = head
    temp = head.next
    print_linked_list_in_reverse(temp)
    print(currentHead)


print_linked_list(node1)
print("Reverse list")
print_linked_list_in_reverse(node1)
