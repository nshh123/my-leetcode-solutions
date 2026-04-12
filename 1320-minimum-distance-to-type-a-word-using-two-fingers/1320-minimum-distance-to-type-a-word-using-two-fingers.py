class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
        
        dp = [0] * 26
        total_dist = 0
        max_save = 0
        
        for i in range(len(word) - 1):
            b = ord(word[i]) - 65
            c = ord(word[i + 1]) - 65
            
            for a in range(26):
                dp[b] = max(dp[b], dp[a] + dist(b, c) - dist(a, c))
                
            max_save = max(max_save, dp[b])
            total_dist += dist(b, c)
            
        return total_dist - max_save