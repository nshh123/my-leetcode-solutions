class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        return min(abs(i - start) for i, num in enumerate(nums) if num == target)