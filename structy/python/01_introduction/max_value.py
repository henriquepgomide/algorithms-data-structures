"""
max value

Write a function, max_value, that takes in list of numbers as an argument. The
function should return the largest number in the list.

Solve this without using any built-in list methods.

You can assume that the list is non-empty.
"""


def max_value(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
