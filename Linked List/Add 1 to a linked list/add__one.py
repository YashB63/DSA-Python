class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def add_one(head):
    dummy_node = Node(0)  
    dummy_node.next = head
    current = dummy_node

    
    while head:
        if head.data != 9:
            current = head
        head = head.next

    
    current.data += 1
    current = current.next

    
    while current:
        current.data = 0
        current = current.next

    
    if dummy_node.data == 0:
        return dummy_node.next

    return dummy_node


def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()



head = Node(1)
head.next = Node(9)
head.next.next = Node(9)
head.next.next.next = Node(9)

print("Original linked list:")
print_list(head)

head = add_one(head)

print("After adding 1:")
print_list(head)
