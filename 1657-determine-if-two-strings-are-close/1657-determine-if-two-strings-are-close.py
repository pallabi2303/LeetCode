class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        diction1=Counter(word1)
        diction2=Counter(word2)
        check=True
        if diction1.keys()==diction2.keys():
            check=check and True
        else :
            check=check and False
            return False
        if sorted(diction1.values()) == sorted(diction2.values()):
            check=check and True
        else:
            return False
        return check
        