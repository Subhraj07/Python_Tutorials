# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

# Node class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    '''
        +----+------+     +----+------+     +----+------+      +----+------+
        | A  | None |     | B  | None |     |  C | None |      |  D | None |
        +----+------+     +----+------+     +----+------+      +----+------+
        
        A -> B -> C -> D -> 0 (Linked list)
        D -> C -> B -> A -> 0 (Reverse Lined List) / A <- B <- C <- D <- 0
    '''
    def reverse(self):
        prev = None
        current = self.head                 # Suppose B
        while current is not None:
            next = current.next             # C
            current.next = prev             # A [ next ]   B -> A
            prev = current                  # B [ prev ]
            current = next                  # C [ Current ] C -> B -> A
        self.head = prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

    print("Given Linked List")
    llist.printList()
    llist.reverse()
    print("\nReversed Linked List")
    llist.printList()
