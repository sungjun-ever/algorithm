from typing import List
#
#
# def reverseString(self, s:List[str]) -> None:
#     left, right = 0, len(s) -1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1


# def reverseString(self, s:List[str]) -> None:
#     s.reverse()


def reverseString(self, s:List[str]) -> None:
    # s = s[::-1]
    s[:] = s[::-1]