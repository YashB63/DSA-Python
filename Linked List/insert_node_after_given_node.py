class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    def addFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def insertAfter(self, previous_node, new_data):
        if previous_node is None:
            print("The previous node must be in Linked List")
            return
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node
        