class Solution:
    def reverseWords(self, s: str) -> str:
        li=s.split()
        li.reverse()
        s1=' '.join(li)
        return s1
        