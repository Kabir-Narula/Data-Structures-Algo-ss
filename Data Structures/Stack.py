class Stack:
    def __init__(self):
        self.head = None  # Stack is empty at first

    # Push an element to the stack (add to the front)
    def push(self, data):
        new_node = Node(data)  # Create a new node with data
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Make the new node the head (top of stack)

    # Pop an element from the stack (remove from the front)
    def pop(self):
        if self.head is None:  # Stack is empty
            return None
        popped = self.head.data  # Get the data from the top (head)
        self.head = self.head.next  # Move the head to the next node
        return popped  # Return the popped value

    # Check if the stack is empty
    def is_empty(self):
        return self.head is None

    # Peek at the top element (without removing it)
    def peek(self):
        if self.head is None:
            return None
        return self.head.data
