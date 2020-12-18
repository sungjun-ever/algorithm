# def is_palindrome(self, s:str) -> bool:
#     strs = []
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#
#     while len(strs) > 1:
#         if strs.pop(0) != strs.pop():
#             return False
#
#     return True

# import collections
# from typing import Deque
#
#
# def is_palindrome(self, s:str) -> bool:
#     strs : Deque = collections.deque()
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#
#     while len(strs) > 1:
#         if strs.popleft() != strs.pop():
#             return False
#
#     return True

import re


def is_palindrome(self, s:str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]