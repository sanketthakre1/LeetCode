class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1=0
        for i in nums1:
            if i in nums2:
                count1=count1+1
        count2=0        
        for j in nums2:
            if j in nums1:
                count2=count2+1
        l=[]        
        l.append(count1)
        l.append(count2)
        return l