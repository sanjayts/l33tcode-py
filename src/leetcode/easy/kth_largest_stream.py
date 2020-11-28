# https://leetcode.com/problems/kth-largest-element-in-a-stream
from bisect import insort
from heapq import heapify, heappushpop, heappop, heappush
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        insort(self.nums, val)
        return self.nums[-self.k]


class KthLargestBetter:

    # https://lenchen.medium.com/leetcode-703-kth-largest-element-in-a-stream-194ceb1572
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapify(self.nums)
        while len(self.nums) > k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) == self.k:
            heappushpop(self.nums, val)
        else:
            heappush(self.nums, val)
        return self.nums[0]