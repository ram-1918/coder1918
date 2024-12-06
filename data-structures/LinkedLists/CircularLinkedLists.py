'''
1. Circularly single linked lists
2. Circularly Double linked lists
'''

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node_at_begining(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def insert_node_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    
    def traverse_nodes(self):
        if not self.head:
            print('Empty list')
            return
        current = self.head
        nodes_list = []
        while True:
            nodes_list.append(f'{current.value}')
            current = current.next
            if current == self.head:
                break
        if nodes_list:
            nodes_list.append(f'{self.head.value}')
        print(' -> '.join(nodes_list))
