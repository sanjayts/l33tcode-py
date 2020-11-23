import pytest

from leetcode.easy.last_stone import Solution


@pytest.mark.parametrize("stones, weight", [
    ([2, 7, 4, 1, 8, 1], 1)
])
def test_last_stone_weight(stones, weight):
    s = Solution()
    assert s.lastStoneWeight(stones) == weight
