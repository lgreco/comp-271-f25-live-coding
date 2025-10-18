from Node import Node


class DoublyLinkedList:

    def __init__(self):
        """Initializes an empty doubly linked list."""
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __str__(self):
        """Returns a string representation of the list."""
        return self.__repr__()

    def __repr__(self):
        """Returns a string representation of the list."""
        # Build a list of node string representations
        nodes = []
        # Traverse the list from head to tail
        current = self.__head
        # Append each node's string representation to the list
        while current is not None:
            nodes.append(str(current))
            current = current.get_next()
        # Join the node strings with " <-> " and return the result
        return " <-> ".join(nodes)

    def is_empty(self):
        """Returns True if the list is empty, False otherwise."""
        return self.__size == 0

    def get_size(self):
        """Returns the number of nodes in the list."""
        return self.__size

    def add_to_back(self, data):
        """Adds a new node with the given data to the back of the list."""
        # Create a new node
        new_node = Node(data)
        # If the list is empty, set the head to the new node
        if self.is_empty():
            self.__head = new_node
        else:
            # Link the new node to the current tail
            new_node.set_prev(self.__tail)
            # Link the current tail to the new node
            self.__tail.set_next(new_node)
        # Update the tail to the new node
        self.__tail = new_node
        # Increment the size of the list
        self.__size += 1

    def add_to_front(self, data):
        """Adds a new node with the given data to the front of the list."""
        # Create a new node
        new_node = Node(data)
        # If the list is empty, set the tail to the new node
        if self.is_empty():
            self.__tail = new_node
        else:
            # Link the new node to the current head
            new_node.set_next(self.__head)
            # Link the current head to the new node
            self.__head.set_prev(new_node)
        # Update the head to the new node
        self.__head = new_node
        # Increment the size of the list
        self.__size += 1

    def find_middle(self):
        """Returns the middle node of the list. If the list has an even number of nodes,
        the second middle node is returned.
        """
        # Prepare an empty variable to hold the middle node
        middle_node = None
        # Check if the list is empty, and if so return the None object
        if not self.is_empty():
            # Set two pointers, one starting at the head and the other at the tail
            forward = self.__head
            backward = self.__tail
            # Move the pointers toward each other until they meet or cross
            while forward != backward and forward.get_next() != backward:
                forward = forward.get_next()
                backward = backward.get_prev()
            middle_node = forward
        return middle_node

    def has_loop(self) -> bool:
        """Returns True if the list has a loop, False otherwise.
        A loop exists if the next pointer of the tail points to the head,
        and the previous pointer of the head points to the tail.
        """
        return (
            self.__head is not None
            and self.__head.has_prev()
            and self.__tail is not None
            and self.__tail.has_next()
            and self.__head.get_prev() == self.__head
            and self.__tail.get_next() == self.__tail
        )
    def has_gap_backward(self):
        """Returns True if there is a gap between the forward and 
        backward pointers."""
        # Assume there is no gap
        has_gap = False
        if not self.is_empty():
            # Operate only on a non empty list, by traversing from head to tail
            cursor = self.__head
            # Move forward through the list until we reach the end or find a gap
            while cursor is not None and cursor.has_next() and not has_gap:
                # Get the next node
                next = cursor.get_next()
                # Check if the next node's previous pointer points back to 
                # the current node. If not, we have found a gap
                has_gap = next.get_prev() != cursor
                # Move the cursor forward
                cursor = next
        return has_gap

    def has_gap_forward(self):
        """Returns True if there is a gap between the backward and
        forward pointers."""
        # Assume there is no gap
        has_gap = False
        # Operate only on a non empty list, by traversing from tail to head
        if not self.is_empty():
            # Start at the tail
            cursor = self.__tail
            # Move backward through list until we reach the start or find a gap
            while cursor is not None and cursor.has_prev() and not has_gap:
                prev = cursor.get_prev()
                has_gap = prev.get_next() != cursor
                cursor = prev
        return has_gap

    def has_gap(self):
        """Returns True if there is a gap in either direction."""
        return self.has_gap_backward() or self.has_gap_forward()

    # Can forward or backward done in single method? Not required for this assignment
    # this is just "Leo stuff"
    def has_gap_in_direction(self, forward=True):
        has_gap = False
        if not self.is_empty():
            # Set the cursor to the start or end based on direction
            cursor = self.__tail if forward else self.__head
            # Define the direction and opposite functions based on the 
            # traversal direction
            direction = (
                (lambda node: node.get_prev())
                if forward
                else (lambda node: node.get_next())
            )
            # 
            opposite = (
                (lambda node: node.get_next())
                if forward
                else (lambda node: node.get_prev())
            )
            # Traverse the list in the specified direction until we find a gap
            while (cursor is not None 
                   and direction(cursor) is not None 
                   and not has_gap):
                # Get the next node in the specified direction
                next = direction(cursor)
                # Check if the opposite pointer of the next node points 
                # back to the current node
                has_gap = opposite(next) != cursor
                # Move the cursor in the specified direction
                cursor = next
        return has_gap
