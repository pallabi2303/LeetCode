class Solution:
    def check(self, nums: List[int]) -> bool:
        temp=sorted(nums)
        double_nums = nums + nums
        n = len(nums)
        
        for i in range(n):
            if double_nums[i:i+n] == temp:
                return True
        return False
        