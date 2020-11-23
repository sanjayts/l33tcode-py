# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique_nums = set(nums)
        for (idx, n) in enumerate(nums):
            needed = target - n
            try:
                idx2 = nums.index(needed, idx + 1)
                return [idx, idx2]
            except ValueError:
                continue
