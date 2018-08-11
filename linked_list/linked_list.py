"""Linked List
"""
import itertools
from collections import namedtuple


class MyCounter():
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


class SinglyLinkedNode():
    def __init__(self, value):
        self.val = value
        self.next = None

    def __repr__(self):
        return f'Node(value = {self.val})'


class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            next_node = self.current
            self.current = self.current.next
            return next_node

    def __eq__(self, other):
        for left, right in itertools.zip_longest(self, other, fillvalue = None):
            try:
                if left.val != right.val:
                    return False
            except AttributeError:
                return False
        return True

    def __repr__(self):
        values = list(map(lambda n: n.val, iter(self)))
        return f'SinglyLinkedList(vals = {values})'

    def __len__(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

    def insert(self, value):
        if self.head is None:
            self.head = SinglyLinkedNode(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = SinglyLinkedNode(value)

    def insert_at_head(self, value):
        to_insert = SinglyLinkedNode(value)
        to_insert.next = self.head
        self.head = to_insert

    def kth_to_last(self, k):
        return self.__kth_to_last(self.head, k, MyCounter())

    def __kth_to_last(self, current, k, counter):
        if current is None:
            return None

        node = self.__kth_to_last(current.next, k, counter)
        counter.increment()

        if counter.count == k:
            return current

        return node

    def pad_to_length(self, length, pad_value):
        while len(self) < length:
            self.insert_at_head(pad_value)


def reverse_addition(a, b):
    added = SinglyLinkedList()
    carry = 0
    for left, right in itertools.zip_longest(a, b, fillvalue = SinglyLinkedNode(0)):
        total = left.val + right.val + carry
        remainder = total % 10
        carry = total // 10
        added.insert(remainder)
    if carry != 0:
        added.insert(carry)
    return added


def forward_addition(left, right):
    def _forward(left_node, right_node):
        if left_node is None and right_node is None:
            return SinglyLinkedList(), 0
        else:
            partial_sum, carry = _forward(left_node.next, right_node.next)
            total = left_node.val + right_node.val + carry
            partial_sum.insert_at_head(total % 10)
            return partial_sum, total // 10

    left_old_head = left.head
    right_old_head = right.head

    max_length = max(len(left), len(right))
    left.pad_to_length(max_length, pad_value = 0)
    right.pad_to_length(max_length, pad_value = 0)

    summed, carry = _forward(left.head, right.head)

    if carry != 0:
        summed.insert_at_head(carry)

    left.head = left_old_head
    right.head = right_old_head
    return summed
