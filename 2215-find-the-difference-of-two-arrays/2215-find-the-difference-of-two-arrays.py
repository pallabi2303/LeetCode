class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1=set(nums1)
        n2=set(nums2)
        answers=[[],[]]
        answers[0]=list(n1-n2)
        answers[1]=list(n2-n1)
        return answers
        
        
        