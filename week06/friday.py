

def remove_element(from_list: list, position: int) -> list:
    """Removes an element from a list at the given position."""
    # Create a copy of the original list
    temp = from_list
    # Only proceed if the position is valid and the list is not None
    # otherwise, the original list is returned
    if from_list is not None and 0 <= position < len(from_list):
        # Create a new list with one less element
        temp = [None] * (len(from_list) - 1)
        # Copy elements from the original list to the new list,
        # skipping the element at the specified position
        for i in range(len(from_list)):
            if i < position:
                temp[i] = from_list[i]
            elif i > position:
                # Skipping is done here by copying the element
                # from the original list to one position earlier
                temp[i - 1] = from_list[i]
    return temp

# Simple test
data = ["Frodo", "Sam", "Merry", "Pippin", "Gandalf", "Aragorn", "Legolas", "Gimli"]
CLEAR_SCREEN = "\033[2J"
print(CLEAR_SCREEN)
print(data)
data = remove_element(data, 3)
print(data)