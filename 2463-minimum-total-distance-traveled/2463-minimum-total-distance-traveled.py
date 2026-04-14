class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        positions = []
        for pos, limit in factory:
            positions.extend([pos] * limit)
        
        n, m = len(robot), len(positions)
        dp = [0] * (m + 1)
        
        for i in range(n):
            next_dp = [float('inf')] * (m + 1)
            for j in range(1, m + 1):
                cost = abs(robot[i] - positions[j - 1])
                next_dp[j] = min(next_dp[j - 1], dp[j - 1] + cost)
            dp = next_dp
            
        return dp[m]