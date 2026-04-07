from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        l=[d for d in range(1,len(nums)+1)]
        setA=set(nums)
        setB=set(l)
        setC=setB-setA
        j=list(setC)
        count=Counter(nums)
        for key in count.keys():
            if count[key]==2:
                return [key,j[0]]

