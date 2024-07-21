class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        slidingwindo=0
        for i in arr:
            if i%2==0:
                slidingwindo=0
            else:
                slidingwindo+=1
                if slidingwindo==3:
                    return True
        return False
        