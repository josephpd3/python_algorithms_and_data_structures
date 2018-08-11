"""Binary Search Tree
"""
class BSTNode():
    def __init__(self, key, p = None, left = None, right = None):
        self.key = key
        self.p = p
        self.left = left
        self.right = right


class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        to_insert = BSTNode(value)

        if self.root is None:
            self.root = to_insert
        else:
            # recursive insert
            self.__insert(self.root, to_insert)

    def __insert(self, current, to_insert):
        # current -> non-None node
        if current.key > to_insert.key:
            if current.left is None:
                current.left = to_insert
            else:
                self.__insert(current.left, to_insert)
        else:
            if current.right is None:
                current.right = to_insert
            else:
                self.__insert(current.right, to_insert)

    def inorder_walk(self):
        yield from self.__inorder_walk(self.root)

    def __inorder_walk(self, current):
        if current is None:
            return
        else:
            yield from self.__inorder_walk(current.left)
            yield current.key
            yield from self.__inorder_walk(current.right)

    def search(self, target):
        return self.__search(self.root, target)

    def __search(self, current, target):
        if current.key == target:
            return current
        elif current.key > target:
            if current.left is not None:
                return self.__search(current.left, target)
        else:
            if current.right is not None:
                return self.__search(current.right, target)
        return None

    def iterative_search(self, target):
        current = self.root
        while current is not None and current.key != target:
            if current.key > target:
                current = current.left
            else:
                current = current.right
        return current
