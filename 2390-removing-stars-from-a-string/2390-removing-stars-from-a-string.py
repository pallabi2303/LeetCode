class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        li=[]
        for i in s:
            if i=='*':
                li.pop(-1)
            else:
                li.append(i)
        newStr=''.join(li)
        return newStr
                
        