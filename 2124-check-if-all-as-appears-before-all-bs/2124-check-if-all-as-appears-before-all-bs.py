class Solution:
    def checkString(self, s: str) -> bool:
        last_a_position = -1
        first_b_position = len(s)
        
        for i in range(len(s)):
            if s[i] == 'a':
                last_a_position = i
            elif s[i] == 'b':
                first_b_position = min(first_b_position, i)
        
            if last_a_position > first_b_position:
                return False
        
        return True