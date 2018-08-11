import pytest
from linked_list.linked_list import (
    forward_addition,
    reverse_addition,
    SinglyLinkedList,
    SinglyLinkedNode
)

num_list = [42, 53, 61, 34, 23, 51, 72]

@pytest.fixture
def get_singly_linked_list():
    def factory(seed = num_list):
        l = SinglyLinkedList()
        for num in seed:
            l.insert(num)
        return l
    return factory


def test_iter(get_singly_linked_list):
    my_list = get_singly_linked_list()

    nums_reversed = list(reversed(num_list))

    for node in my_list:
        assert node.val == nums_reversed.pop()


def test_len(get_singly_linked_list):
    my_list = get_singly_linked_list()
    target_length = len(num_list)
    assert len(my_list) == target_length


def testt_eq(get_singly_linked_list):
    one_two_three = get_singly_linked_list([1, 2, 3])
    one_two_three_four = get_singly_linked_list([1, 2, 3, 4])

    assert one_two_three == get_singly_linked_list([1, 2, 3])
    assert one_two_three != one_two_three_four


def test_kth_to_last(get_singly_linked_list):
    my_list = get_singly_linked_list()

    third_from_last = num_list[-3]

    assert my_list.kth_to_last(3).val == third_from_last


def test_list_addition_reverse(get_singly_linked_list):
    one_thirty_seven = [7, 3, 1]
    one_thousand_two_twenty_five = [5, 2, 2, 1]
    list_a = get_singly_linked_list(one_thirty_seven)
    list_b = get_singly_linked_list(one_thousand_two_twenty_five)

    one_thousand_three_sixty_two = [2, 6, 3, 1]

    assert reverse_addition(
        list_a,
        list_b
    ) == get_singly_linked_list(one_thousand_three_sixty_two)


def test_list_addition_forward(get_singly_linked_list):
    one_thirty_seven = [1, 3, 7]
    one_thousand_two_twenty_five = [1, 2, 2, 5]
    list_a = get_singly_linked_list(one_thirty_seven)
    list_b = get_singly_linked_list(one_thousand_two_twenty_five)

    one_thousand_three_sixty_two = [1, 3, 6, 2]

    assert forward_addition(
        list_a,
        list_b
    ) == get_singly_linked_list(one_thousand_three_sixty_two)
