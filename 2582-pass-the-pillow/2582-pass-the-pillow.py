class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = 2 * (n - 1)
        remainder = time % cycle_length
    
        if remainder < n:
            return 1 + remainder
        else:
            return n - (remainder - (n - 1))
        