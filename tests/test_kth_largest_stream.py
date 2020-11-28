from typing import List, Tuple

import pytest
from leetcode.easy.kth_largest_stream import KthLargest, KthLargestBetter


@pytest.mark.parametrize("nums, k, pairs, klass", [
    ([4, 5, 8, 2], 3, [(3, 4), (5, 5), (10, 5), (9, 8), (4, 8)], KthLargest),
    ([4, 5, 8, 2], 3, [(3, 4), (5, 5), (10, 5), (9, 8), (4, 8)], KthLargestBetter)
])
def test_add(nums: List[int], k: int, pairs: List[Tuple[int, int]], klass):
    o = klass(k, nums)
    for (added, expected) in pairs:
        print(f'Processing pair (#{added}, #{expected})')
        assert o.add(added) == expected
