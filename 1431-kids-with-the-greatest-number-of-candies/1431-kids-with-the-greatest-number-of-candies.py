class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        maxcand=max(candies)
        for i in candies:
            m=i+extraCandies
            if m>=maxcand:
                result.append(True)
            else:
                result.append(False)
        return result
        