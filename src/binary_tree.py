IN_ORDER = "in_order"
PRE_ORDER = "pre_order"
POS_ORDER = "pos_order"
LEVEL_ORDER = "level_order"


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BinaryTreeNode(value)
            return

        current = self.root
        queue = [current]

        while len(queue):
            current = queue.pop(0)

            if current.left is None:
                current.left = BinaryTreeNode(value)
                return

            elif current.right is None:
                current.right = BinaryTreeNode(value)
                return

            queue.append(current.left)
            queue.append(current.right)

    def find(self, value):
        if self.root is None:
            raise Exception("Empty tree!")

        current = self.root
        queue = [current]

        while len(queue):
            current = queue.pop(0)

            if current.value == value:
                return current

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        raise Exception("Data not found!")

    def delete(self, value):
        if self.root is None:
            raise Exception("Empty tree!")

        if self.root.value == value:
            self.root = None
            return

        parent = self.root
        queue = [(parent, parent.left), (parent, parent.right)]
        level_order_list = self.get_level_order_list()

        while len(queue):
            parent, current = queue.pop(0)

            if current.value == value:
                if parent.left is current:
                    parent.left = None
                    break

                elif parent.right is current:
                    parent.right = None
                    break

            queue.append((current, current.left))
            queue.append((current, current.right))

        self.root = None
        level_order_list.remove(value)
        self.generate_from_ordered_list(level_order_list)

    def generate_from_ordered_list(self, level_order_list):
        for i in level_order_list:
            self.insert(i)
        
    def get_level_order_list(self):
        if self.root is None:
            raise Exception("Empty tree!")

        current = self.root
        queue = [current]
        level_order_list = []

        while len(queue):
            current = queue.pop(0)
            level_order_list.append(current.value)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        return level_order_list

    def print_transversal(self, current_node=None, type=IN_ORDER, init=True):
        if self.root is None:
            print("Empty Tree!")
            return

        if init:
            current_node = self.root

        if current_node is None:
            return

        if type == IN_ORDER:
            self.print_transversal(current_node.left, IN_ORDER, False)
            print(current_node.value)
            self.print_transversal(current_node.right, IN_ORDER, False)

        elif type == PRE_ORDER:
            print(current_node.value)
            self.print_transversal(current_node.left, PRE_ORDER, False)
            self.print_transversal(current_node.right, PRE_ORDER, False)

        elif type == POS_ORDER:
            self.print_transversal(current_node.left, POS_ORDER, False)
            self.print_transversal(current_node.right, POS_ORDER, False)
            print(current_node.value)

        elif type == LEVEL_ORDER:
            self._print_level_transversal()

    def _print_level_transversal(self):
        current = self.root
        queue = [current]

        while len(queue):
            current = queue.pop(0)
            print(current.value)

            if current.left is not None:
                queue.append(current.left)
                
            if current.right is not None:
                queue.append(current.right)
