# push_front - add an item to the front of the linked list
# push_back - add an item to the back of the linked list
# pop_front - remove the frontmost item from the linked list
# pop_back - remove the backmost item from the linked list
# insert - given a point within the list insert an item just before that point
# erase - remove a node at a specific point within the list
# erase(a,b) - erases all nodes between a and b
# traversals - some operation that applies to every node in the list


# Define a class for a node in the linked list
class Node:
    def __init__(self, data):
        # Each node has two attributes: data (to store the value) and next (to point to the next node)
        self.data = data
        self.next = None  # Initialize next as None, meaning it's the last node for now

# Define the LinkedList class that will manage the nodes
class LinkedList:
    def __init__(self):
        # Initialize the linked list with a head pointer set to None (empty list)
        self.head = None

    # Function to add a node at the front of the list
    def push_front(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # The new node's next pointer should point to the current head
        self.head = new_node  # Update the head to be the new node
        print(f"Pushed {data} to the front")

    # Function to add a node at the back of the list
    def push_back(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = new_node
            print(f"Pushed {data} to the back (as the only element)")
            return
        # Otherwise, traverse the list to find the last node
        last = self.head
        while last.next:
            last = last.next  # Move to the next node
        last.next = new_node  # Set the next of the last node to the new node
        print(f"Pushed {data} to the back")

    # Function to remove the frontmost node from the list
    def pop_front(self):
        if not self.head:
            print("List is empty. Cannot pop front.")
            return
        pop_value = self.head.data  # Store the value of the node being removed
        self.head = self.head.next  # Move the head to the next node
        print(f"Popped {pop_value} from the front")

    # Function to remove the last node from the list
    def pop_back(self):
        if not self.head:
            print("List is empty. Cannot pop back.")
            return
        if not self.head.next:
            # If there's only one node, remove it and set head to None
            pop_value = self.head.data
            self.head = None
            print(f"Popped {pop_value} from the back (last element)")
            return
        # Otherwise, traverse to find the second-to-last node
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next  # Move to the next node
        pop_value = second_last.next.data  # Store the value of the last node
        second_last.next = None  # Remove the last node
        print(f"Popped {pop_value} from the back")

    # Function to insert a node before a given position (data_before)
    def insert(self, data_before, data):
        if not self.head:
            print("List is empty. Cannot insert before a node.")
            return
        new_node = Node(data)
        if self.head.data == data_before:
            # If the node to insert before is the head, use push_front
            self.push_front(data)
            return
        current = self.head
        while current.next and current.next.data != data_before:
            current = current.next  # Traverse the list
        if current.next is None:
            print(f"Node with data {data_before} not found.")
        else:
            # Insert the new node before the node with data_before
            new_node.next = current.next
            current.next = new_node
            print(f"Inserted {data} before {data_before}")

    # Function to remove a specific node by value
    def erase(self, value):
        if not self.head:
            print("List is empty. Cannot erase.")
            return
        if self.head.data == value:
            # If the node to erase is the head, just pop the front
            self.pop_front()
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next  # Traverse the list
        if current.next is None:
            print(f"Node with data {value} not found.")
        else:
            # Remove the node by skipping it
            erase_value = current.next.data
            current.next = current.next.next
            print(f"Erased node with data {erase_value}")

    # Function to erase all nodes between two positions
    def erase_range(self, start_value, end_value):
        if not self.head:
            print("List is empty. Cannot erase range.")
            return
        current = self.head
        # Find the start node (node before the start_value)
        while current and current.data != start_value:
            prev = current
            current = current.next
        if current is None:
            print(f"Start node with value {start_value} not found.")
            return
        # Now, erase all nodes until we reach end_value or the end of the list
        while current and current.data != end_value:
            print(f"Erasing node with value {current.data}")
            prev.next = current.next  # Skip over the current node
            current = current.next
        print(f"Erased all nodes between {start_value} and {end_value}")

    # Function to traverse the list and apply an operation (here we just print the values)
    def traverse(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(f"Node data: {current.data}")
            current = current.next

# Usage example
ll = LinkedList()

# Adding elements
ll.push_front(10)
ll.push_back(20)
ll.push_back(30)
ll.push_front(5)

# Traversing the list
ll.traverse()

# Inserting element
ll.insert(20, 15)

# Removing elements
ll.pop_front()
ll.pop_back()

# Erasing specific element
ll.erase(15)

# Erasing a range of elements
ll.erase_range(10, 30)

# Final traversal
ll.traverse()
