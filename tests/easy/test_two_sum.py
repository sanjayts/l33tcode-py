from typing import List

import pytest
from leetcode.easy.two_sum import Solution


@pytest.mark.parametrize("nums, target, expected", [
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1])
])
def test_two_sum(nums: List[int], target: int, expected: List[int]):
    s = Solution()
    assert s.twoSum(nums, target) == expected
