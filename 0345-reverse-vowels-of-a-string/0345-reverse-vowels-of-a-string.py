class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels='aeiouAEIOU'
        ind=[]
        lt=[]
        strli=list(s)
        n=len(s)
        for i in range(n):
            if s[i] in vowels:
                ind.append(i)
                lt.insert(0,s[i])
        size=len(ind)
        for i in range(size):
            strli[ind[i]]=lt[i]
        return ''.join(strli)
        