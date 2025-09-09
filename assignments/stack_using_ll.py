class MyStack:

    # class StackNode:

    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
        
    # main trick - insert & delete at head
    #Function to push an integer into the stack.
    def __init__(self):
        self.head = None
    
    def push(self, data):

        # Add code here
        new_node = StackNode(data)
        new_node.next = self.head
        self.head = new_node

    #Function to remove an item from top of the stack.
    def pop(self):

        # Add code here
        if not self.head:
            return -1
        popped = self.head.data
        self.head = self.head.next
        return popped
