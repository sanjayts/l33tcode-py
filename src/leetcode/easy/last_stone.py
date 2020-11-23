# https://leetcode.com/problems/last-stone-weight/

from typing import List
import heapq


class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [s * -1 for s in stones]
        heapq.heapify(new_stones)
        return Solution._internal(new_stones)

    @staticmethod
    def _internal(stones: List[int]) -> int:
        if len(stones) > 1:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            diff = abs(a - b)
            if diff != 0:
                heapq.heappush(stones, diff * -1)
            return Solution._internal(stones)
        elif len(stones) == 1:
            return -1 * stones[0]
        else:
            return 0
