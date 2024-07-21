class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            pre=sum(nums[0:i])
            post=sum(nums[i+1:len(nums)])
            if pre==post:
                return i
        return -1
        