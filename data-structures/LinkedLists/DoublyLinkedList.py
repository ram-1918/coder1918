class Node():
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
    
    ''' Insertion of Nodes '''
    def insert_node_at_begining(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_node_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            # 1 <-> 2 <-> 3 <-> 4 <-> None
            current = self.head
            # traverse until last but one node
            # make current to point to node 4
            while current.next:
                current = current.next
            # By here, current = 4
            current.next = new_node
            new_node.prev = current

    def insert_node_at_index(self, value, k):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            if k == 1:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                current = self.head
                # 1 <-> 2 <-> 3 <-> 4 <-> None
                # current = 1, k = 3
                # k > 2, makes the current pointer arrive at the (k - 1) th position
                while current and k > 2:
                    print(current.value)
                    current = current.next
                    k -= 1
                # current = 2, new_node = 1000
                temp = current.next
                new_node.next = current.next      # 1 -> 2   1000 -> 3
                current.next = new_node           # 2 -> 1000 -> 3
                new_node.prev = current           # 2 <-> 1000 -> 3
                temp.prev = new_node              # 2 <-> 1000 <-> 3

    ''' Deletion of Nodes'''
    def delete_node_from_begining(self):
        if self.head is None:
            return
        # Check if next node exists, since we need to move head to next pointer
        elif self.head.next:
            temp = self.head.next
            self.head.next = None
            temp.prev = None
            self.head = temp
        else:
            self.head = None

    def delete_node_from_end(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            
            # at this step, current points to last node,
            # Drop the connection with the last node
            if current.prev:
                current.prev.next = None
                current.prev = None
            # check if prev node exists, since we need it detach from the previous node
            else:
                self.head = None

    def delete_node_at_index(self, k):
        if self.head is None:
            print("delete operation not supported")
            return
        
        if k == 1:
            if self.head.next:
                temp = self.head.next
                temp.prev = None
                self.head = temp
            else:
                self.head = None
            return
        
        # Traverse until (k - 1)th node
        current = self.head
        for _ in range(k - 2):
            if not current.next:
                print('k out of bounds')
                return
            current = current.next
        
        # At this point, current points to (k - 1)th node
        target = current.next
        if target:
            current.next = target.next
            if target.next:
                target.next.prev = current

    ''' Updation of nodes '''
    def update_node_at_index(self, new_value, k):
        if self.head is None:
            return
        else:
            current = self.head
            while current and k > 1:
                current = current.next
                k  -= 1
            if current:
                current.value = new_value
            else:
                print('Not possible to update')

    ''' Traversal of nodes '''
    def traverse_nodes(self, reverse=False):
        current = self.head
        nodes = ['None']
        while current:
            nodes.append(f'{current.value}')
            current = current.next
        if len(nodes) > 1:
            nodes.append('None')
        print(' <-> '.join(nodes))

    def reverse_traverse_nodes(self):
        if self.head is None:
            print('No nodes found')
            return
        current = self.head
        # Traverse until the tail
        while current.next:
            current = current.next
        
        # collect nodes values in reverse order
        rev_nodes = ['None']
        while current:
            rev_nodes.append(f'{current.value}')
            current = current.prev
        
        if len(rev_nodes) > 1:
            rev_nodes.append('None')
        print(' <-> '.join(rev_nodes))