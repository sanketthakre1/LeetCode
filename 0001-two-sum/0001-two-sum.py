class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in nums:
            for j in range((nums.index(i))+1,len(nums)):
                if((i+nums[j]==target)):
                    if (j and nums.index(i))  not in l:

                        l.append(nums.index(i))
                        l.append(j)
        return l
