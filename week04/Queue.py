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
        success = self._usage < self._capacity
        if success:
            self._underlying[self._usage] = value
            self._usage += 1
        return success

    def remove(self):
        # We can only remove from the front of the queue
        removed = self._underlying[0]
        if self._usage > 0:
            # shift everything from [1] to [usage-1] one position to the left
            for i in range(1, self._usage):
                self._underlying[i - 1] = self._underlying[i]
            # make [usage-1] null
            self._underlying[self._usage-1] = None
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
        return f"{self._underlying}"
    
if __name__ == "__main__":
    test = Queue(4)
    print(test)
    print(test.add("Sam"))
    print(test.add("Frodo"))
    print(test.add("Gandalf"))
    print(test.add("Leo"))
    print(test.add("Sauron"))
    print(test)
    print(test.remove())
    print(test)