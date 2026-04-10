from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices_map = defaultdict(list)
        for i, num in enumerate(nums):
            indices_map[num].append(i)
            
        dist = float('inf')
        
        for indices in indices_map.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    l = indices[i:i+3]
                    d = abs(l[0]-l[1]) + abs(l[1]-l[2]) + abs(l[2]-l[0])
                    dist = min(dist, d)
                    
        return dist if dist != float('inf') else -1