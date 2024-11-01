# Define Node class for the individual elements of the linked list
class Node:
    def __init__(self, data=None):
        """
        Constructor for the Node.
        data: Stores the value of the node.
        next: Points to the next node, default is None.
        """
        self.data = data
        self.next = None

# Define LinkedList class with a sentinel node
class LinkedList:
    def __init__(self):
        """
        Constructor for LinkedList.
        Initializes with a sentinel node and keeps track of the size.
        """
        self.sentinel = Node()  # Sentinel node to mark the beginning
        self.size = 0  # Size to keep track of the number of elements

    def append(self, data):
        """
        Append an element at the end of the list.
        """
        new_node = Node(data)  # Create a new node with the given data
        last = self.sentinel  # Start from the sentinel node
        
        # Traverse to the last node
        while last.next:
            last = last.next
        
        last.next = new_node  # Append new node at the end
        self.size += 1  # Increment size

    def display(self):
        """
        Display the elements of the list.
        """
        current = self.sentinel.next  # Skip the sentinel node
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements) + " -> None")  # Display linked list

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    
    linked_list.display()  # Outputs: 10 -> 20 -> 30 -> None
