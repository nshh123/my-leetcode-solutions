class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        min_dist = [n] * n
        last_seen = {}
        for i in range(n * 2):
            index = i % n
            num = nums[index]
            if num in last_seen:
                prev_index = last_seen[num] % n
                d = i - last_seen[num]
                min_dist[index] = min(min_dist[index], d)
                min_dist[prev_index] = min(min_dist[prev_index], d)
            last_seen[num] = i
        return [-1 if min_dist[q] == n else min_dist[q] for q in queries]