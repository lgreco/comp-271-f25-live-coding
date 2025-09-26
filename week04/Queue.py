class Queue:

    # Unless users specify a capacity, new Queue objects are created with size 4
    _DEFAULT_CAPACITY = 4

    def __init__(self, capacity=_DEFAULT_CAPACITY):
        """Instantiate a Queue object as an underlying list with as many
        elements as the specified capacity, set all these elements to
        None, and indicate that the queue object is empty by setting its
        usage to 0.
        """
        self._capacity = capacity
        self._usage = 0
        self._underlying = [None] * self._capacity

    # --- Basic functionality ---

    def add(self, value: str) -> bool:
        """Add value to the back of the queue. Return True if successful,
        False if the queue is full.
        """
        # We can only add if the queue is not full
        success = self._usage < self._capacity
        if success:
            # Queue is not full, so we can add the value
            self._underlying[self._usage] = value
            # Increment usage
            self._usage += 1
        return success

    def remove(self):
        """Remove and return the value at the front of the queue."""
        # Whatever is at the front of the queue, we'll return. Even if
        # the queue is empty, in which case we'll return None.
        removed = self._underlying[0]
        # If the queue is not empty, we need to shift everything
        if self._usage > 0:
            # shift everything from [1] to [usage-1] one position to the left
            for i in range(1, self._usage):
                self._underlying[i - 1] = self._underlying[i]
            # make [usage-1] null
            self._underlying[self._usage - 1] = None
            # decrease usage
            self._usage -= 1
        return removed

    # --- accessors ---

    def get_capacity(self):
        # encourages programmers from using Queue._usage;
        # instead they should use Queue.get_capacity()
        return self._capacity

    def get_usage(self):
        return self._usage

    def __len__(self):
        # allows calls from function len()
        return self._usage

    def __str__(self):
        return f"Usage/Capacity = {self._usage}/{self._capacity}; {self._underlying}"


if __name__ == "__main__":
    characters = ["Sam", "Frodo", "Gandalf", "Legolas", "Gimli"]
    test_queue = Queue(4)
    for character in characters:
        print(f"Attempting to add {character} to the queue. Addition {"completed" if test_queue.add(character) else "failed"}")
    print(test_queue)
    while len(test_queue) > 0:
        print(f"After removing \"{test_queue.remove()}\", queue is {test_queue}")