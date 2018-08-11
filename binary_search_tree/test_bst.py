import pytest
from binary_search_tree.bst import BST, BSTNode

numbers = [15, 42, 82, 13, 13, 43, -4]
descending_numbers = list(reversed(sorted(numbers)))

@pytest.fixture
def get_tree():
    def factory(to_insert = numbers):
        t = BST()
        for num in to_insert:
            t.insert(num)
        return t
    return factory


def test_insert_and_inorder(get_tree):
    t = get_tree()

    for key in t.inorder_walk():
        assert descending_numbers.pop() == key


def test_search(get_tree):
    t = get_tree()

    for search_method in ('search', 'iterative_search'):
        tree_search = getattr(t, search_method)

        found_result = tree_search(42)
        assert type(found_result) is BSTNode and found_result.key == 42

        not_found_result = tree_search(999)
        assert not_found_result is None
