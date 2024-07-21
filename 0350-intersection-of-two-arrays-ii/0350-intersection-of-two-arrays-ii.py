class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    l1.append(i)
                    nums2.remove(i)
                    break
        return l1
        