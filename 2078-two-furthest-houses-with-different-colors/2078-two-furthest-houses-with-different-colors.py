from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i, j = 0, n - 1
        
        while colors[0] == colors[j]:
            j -= 1
            
        while colors[-1] == colors[i]:
            i += 1
            
        return max(j, n - 1 - i)