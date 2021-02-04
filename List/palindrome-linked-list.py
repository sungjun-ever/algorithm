from collections import deque

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# def is_palindrome() -> bool:
#     lst = [1, 2]
#     head = ListNode(lst[0])
#     q = []
#     i = 0
#
#     if not head:
#         return True
#
#     node = head
#
#     while i < len(lst):
#         node.next = ListNode(lst[i])
#         node = node.next
#         q.append(node.val)
#         i += 1
#
#     while len(q) > 1:
#         if q.pop(0) != q.pop():
#             return False
#
#     return True


def is_palindrome() -> bool:
    lst = [1, 2, 2, 1]
    head = ListNode(lst[0])
    q = deque()
    i = 0

    if not head:
        return True

    node = head

    while i < len(lst):
        node.next = ListNode(lst[i])
        node = node.next
        q.append(node.val)
        i += 1

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True

print(is_palindrome())