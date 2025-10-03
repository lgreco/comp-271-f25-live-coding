class AmazingAndSuperiorSet:

    _DEFAULT_SIZE = 4

    def __init__(self, size: int = _DEFAULT_SIZE):
        self._underlying = [None] * size
        self._usage = 0

    def _exists(self, value) -> bool:
        exists = False
        i = 0
        while i < self._usage and not exists:
            exists = self._underlying[i] == value
            i += 1
        return exists

    def add(self, value):
        """Allows value into the underlying array only if the 
        value does not already exist in the array"""
        if not self._exists(value):
            self._underlying[self._usage] = value
            self._usage += 1

    def __repr__(self):
        return f"{self._underlying}"

if __name__ == "__main__":
    test = AmazingAndSuperiorSet()
    test.add("A")
    test.add("A")
    test.add("A")
    test.add("B")
    test.add("A")
    test.add("A")
    test.add("A")
    test.add("A")
    print(test)
