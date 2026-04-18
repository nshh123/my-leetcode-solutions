from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        pos = {}
        ans = float('inf')
        
        for i, x in enumerate(nums):
            if x in pos:
                ans = min(ans, i - pos[x])
            
            rev_x = int(str(x)[::-1])
            pos[rev_x] = i
            
        return -1 if ans == float('inf') else ans