class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxEle = 0
        for num in nums:
            if num in numSet and -num in numSet:
                maxEle = max(abs(num), maxEle)
        return maxEle if maxEle!=0 else -1