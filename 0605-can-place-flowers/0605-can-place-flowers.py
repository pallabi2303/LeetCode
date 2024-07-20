class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], m: int) -> bool:
        count=0
        n=len(flowerbed)
        if m==0:
            return True
        if n==1:
            if flowerbed[0]==0 and m==1 :
                flowerbed[0]=1
                return True
            else:
                return False
        if n==0:
            return False

        for i in range(n):
            if flowerbed[i]==0:
                if i==0 and flowerbed[i+1]==0 :
                    count+=1
                    flowerbed[i]=1
                elif i==n-1 and flowerbed[i-1]==0:
                    count+=1
                    flowerbed[i]=1
                elif flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    count+=1
                    flowerbed[i]=1
                else : 
                    continue
            if count==m:
                return True
        return False
