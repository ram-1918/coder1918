''' Single linkedlist '''
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    ''' Size of Linkedlist '''

    def sizeOfLL(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        print(f'Size of LL: {size}')
    
        # Traversing linkedlists
    
    ''' Traversing the list '''

    def traverseList(self, head = None, text = 'Traversal'):
        head = self.head if not head else head
        nodesList = []
        while head:
            nodesList.append(f'{head.value} -> ')
            head = head.next
        if not nodesList: 
            print('No nodes found')
        else: 
            print(f"{text}: {''.join(nodesList).strip('-> ')}")

    ''' Insert Operation '''

    def insertNodeAtBegining(self, value):
        newNode = Node(value)
        # If head is empty, make the new node as head
        if self.head is None:
            self.head = newNode
            return
        else:
            # else, insert and update head
            newNode.next = self.head
            self.head = newNode

    def insertNodeAtEnd(self, value):
        newNode = Node(value)
        # If head is empty
        if self.head is None:
            self.head = newNode
            return
        else:
            # Iterate till the end and insert newNode at the end
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        
    def insertNodeAtIndex(self, value, index):
        newNode = Node(value)
        # If head is empty
        if self.head is None:
            self.head = newNode
            return
        else:
            # If index is the 1st position, then it is insert at the beginning
            if index == 1:
                self.insertNodeAtBegining(value)
                return 
            else:
                # Keep track of index with 'position' and update current pointer
                position = 1
                current = self.head
                while current and position != index - 1:
                    position += 1
                    current = current.next
                # At this point, current pointer is at index 4, 
                # so that new Node can be inserted at index 5
                newNode.next = current.next
                current.next = newNode
    
    ''' Delete Operation '''

    def deleteNodeAtBeginning(self):
        if self.head is None:
            return
        else:
            temp = self.head.next
            self.head.next = None
            self.head = temp

    def deleteKNodesFromBegining(self, k = 1):
        if self.head is None:
            return 
        else:
            if k == 1:
                self.deleteNodeAtBeginning()
            else:
                position = 1
                current = self.head
                while current and current.next and position != k:
                    position += 1
                    current = current.next
                temp = current.next
                current.next = None
                self.head = temp
        print(f'Deleted {k} nodes from the beginning')
    
    def deleteNodeAtEnd(self):
        current = self.head
        # If there is only one node
        if current.next is None:
            current = None
        else:
            while current and current.next:
                if current.next.next is None:
                    break
                current = current.next
            nodeValue = current.next.value
            current.next = None
            print(f'Deleted last node {nodeValue}')
    
    def deleteNodeAtIndex(self, k):
        if self.head is None:
            return
        else:
            position = 1
            current = self.head
            if k == 1:
                self.deleteNodeAtBeginning()
                return
            # Traverse until kth but one node
            while current and position != k - 1:
                position += 1
                current = current.next
            temp = current.next.next    # Store (k + 1)th node in temp
            current.next.next = None    # de-reference kth next pointer
            current.next = temp         # Map (k - 1)th node to (k + 1)th node

    ''' Update Operation '''
    
    def updateKthNode(self, k, newValue):
        if self.head is None:
            return 
        current = self.head
        position = 1
        while current and position != k:
            position += 1
            current = current.next
        if current is None:
            print(f'Update: Node not found')
        else:
            current.value = newValue
            print(f'Update: New Value updated: {current.value}')
    
    ''' Reversing nodes iterative, recurrsive '''

    def reverseNodesRecurrsive(self, head):
        if not head or not head.next:
            return head
        rev = self.reverseNodes(head.next)
        head.next.next = head
        head.next = None
        return rev
    
    def reverseNodesIteration(self, head):
        head = self.head
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def reverseKNodes(self, head, k):
        prev = None
        while head and k:
            head.next, prev, head = prev, head, head.next
            k -= 1
        return prev
        

    ''' Linkedlist Cycle detection and handling '''
    # Create a cycle
    def createCycle(self):
        randomNode = self.head.next
        current = self.head
        while current.next:
            current = current.next
        current.next = randomNode
    
    # Remove cycle by disconnecting links
    def removeCycle(self):
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                print(f'Cycle Found')
                fast.next = None
                print(f'Removed Cycle')
                return
        else:
            print(f'No cycle found')

    # Check if cycle is found in the linkedlist
    def cycleDetection(self):
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                print(f'Cycle Found')
                return
        else:
            print(f'No cycle found')

    def findMiddleNode(self):
        if self.head is None:
            return self.head
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.value)


    def reverseKGroup(self, head, k):

        if head is None or k <= 1:
            return None
        
        current = head
        count = 0
        while current and count < k:
            current = current.next
            count += 1

        if count == k:
            rev = self.reverseKNodes(head, k)
            head.next = self.reverseKGroup(current, k)
            return rev
        
        return head
        
  