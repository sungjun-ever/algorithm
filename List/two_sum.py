from typing import List


# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     for i, n in enumerate(nums):
#         complement = target - n
#
#         if complement in nums[i+1:]:
#             return nums.index(n), nums[i+1:].index(complement) + (i+1)


# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     nums_map = {}
#     for i, num in enumerate(nums):
#         nums_map[num] = i
#
#     for i, num in enumerate(nums):
#         if target - num in nums_map and i != nums_map[target - num]:
#             return nums.index(num), nums_map[target - num]


def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i