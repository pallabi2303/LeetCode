import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m=len(str1)
        n=len(str2)
        gcdlen=math.gcd(m,n)
        if set(str1)!=set(str2):
            return ""
        if str1+str2==str2+str1:
            return str1[:gcdlen]
        else:
            return ""
       
        
