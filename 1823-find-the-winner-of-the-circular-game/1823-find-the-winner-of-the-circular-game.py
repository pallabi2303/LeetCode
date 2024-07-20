class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        li=[i for i in range(1,n+1)]
        index=0
        while(len(li)>1):
           index=(index+(k-1))%len(li)
           li.pop(index)
        return li[0]

        