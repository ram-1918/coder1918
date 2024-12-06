''' Linked lists 
Types: Single linkedlists, double linkedlists, circular linkedlists
Complexities
> traverse, access, insert in the middle/end, deletion in the middle/end, update: O(n)
'''

'''
Limitations:
> Memory overhead as it needs to store the pointer to the next node
> sequential access
> due to scattered memory locations, these are cache unfriendliness
> use collections.deque() as it is a doubly linkedlist
> needs to handle pointers with care during insertion, deletion, traversal

Trade-offs:
> just excels in frequent insertions/deletions while implementing stacks/queues
but not for frequent searchs and random access are needed(arrays/hashmaps suits here)
> frequent memory allocation and deallocation

edge-cases:
> Empty linked lists, single node lists(properly update node to none after deletion)
> Cyclic lists, edge cases in deletion, deletion during iteration(use flags or seprate pointers), 

'''

from SinglyLinkedList import SinglyLinkedList
from DoublyLinkedList import DoublyLinkedList
from CircularLinkedLists import CircularLinkedList

if __name__ == '__main__':
    singleLLObj = SinglyLinkedList()
    doubleLLObj = DoublyLinkedList()
    circularLLObj = CircularLinkedList()
    
    # Insert nodes to the linked list
    values = [2,6,8,5,7]
    for value in values:
        singleLLObj.insertNodeAtBegining(value)
        doubleLLObj.insert_node_at_begining(value)
        circularLLObj.insert_node_at_begining(value)

    values = [1,4,6,10]
    for value in values:
        singleLLObj.insertNodeAtEnd(value)
        doubleLLObj.insert_node_at_end(value)


    singleLLObj.traverseList()
    singleLLObj.sizeOfLL()

    singleLLObj.findMiddleNode()

    doubleLLObj.traverse_nodes()
    doubleLLObj.delete_node_at_index(1)
    # doubleLLObj.update_node_at_index(444, 4)
    doubleLLObj.traverse_nodes()
    # doubleLLObj.reverse_traverse_nodes()

    circularLLObj.traverse_nodes()
    
    ''' Reverse Nodes Iterative
    reverseHead = singleLLObj.reverseNodesIteration(head)
    singleLLObj.traverseList(reverseHead)
    '''



    
