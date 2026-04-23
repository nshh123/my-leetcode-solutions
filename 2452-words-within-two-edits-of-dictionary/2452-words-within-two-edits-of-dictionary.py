from typing import List
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        return [q for q in queries if any(sum(c1 != c2 for c1, c2 in zip(q, d)) <= 2 for d in dictionary)]