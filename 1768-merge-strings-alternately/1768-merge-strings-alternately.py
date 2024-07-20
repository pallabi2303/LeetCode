class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=list()
        for i,j in zip(word1,word2):
            l1.append(i)
            l1.append(j)
        if len(word1)>len(word2):
            l1.append(word1[len(word2):])
        if len(word2)>len(word1):
            l1.append(word2[len(word1):])
        sen=''.join(l1)
        return sen