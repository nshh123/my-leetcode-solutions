class Solution:
    def minElement(self, nums: List[int]) -> int:
        min=float('inf')
        for i in nums:
            fn= str(i)
            l=0
            for j in range(0,len(fn)):
                l=l+int(fn[j])
            min=l if l<min else min
        return min
