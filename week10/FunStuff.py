class Node:

    def __init__(self, value):
        self.value = value
        self.count = 0
        self.right = None
        self.left = None
    def __str__(self):
        return f"[{self.value}]"


class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            cursor = self.root
            while (True):
                if new_node.value < cursor.value:
                    # Slide to the left ... tbd
                    if cursor.left is None:
                        cursor.left = new_node
                        break
                    else:
                        cursor = cursor.left
                elif new_node.value > cursor.value:
                    # Slide to the right ...
                    if cursor.right is None:
                        cursor.right = new_node
                        break
                    else:
                        cursor = cursor.right

                else:
                    # Node already exists at cursor
                    cursor.count += 1
                    break

if __name__ == "__main__":
    test = BinaryTree()
    
    test.add("now")
    test.add("is")
    test.add("the")
    test.add("winter")
    print(test.root.right.right)