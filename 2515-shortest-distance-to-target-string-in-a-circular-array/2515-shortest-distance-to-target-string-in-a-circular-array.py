class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        res = n
        
        for i in range(n):
            if words[i] == target:
                dist = abs(i - startIndex)
                res = min(res, dist, n - dist)
                
        return res if res != n else -1