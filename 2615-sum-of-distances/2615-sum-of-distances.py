from typing import List
from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        
        res = [0] * len(nums)
        for indices in pos.values():
            n = len(indices)
            left_sum = 0
            right_sum = sum(indices)
            for i, idx in enumerate(indices):
                right_sum -= idx
                res[idx] = (idx * i - left_sum) + (right_sum - idx * (n - 1 - i))
                left_sum += idx
        return res  