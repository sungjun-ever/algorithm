# def arrayPairSum(nums):
#     sum = 0
#     pair = []
#     nums.sort()
#     for n in nums:
#         pair.append(n)
#         if len(pair) == 2:
#             sum += min(pair)
#             pair = []
#
#     return sum


# def arrayPairSum(nums):
#     sum = 0
#     nums.sort()
#     for i, n in enumerate(nums):
#         if i % 2 == 0:
#             sum += n
#     return sum


def arrayPairSum(nums):
    return sum(sorted(nums)[::2])

nums = [1, 4, 3 ,2]
r = arrayPairSum(nums)
print(r)