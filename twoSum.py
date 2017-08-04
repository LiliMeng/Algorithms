"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

@author: lili
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict={}
        my_set= set()
        for i in range(len(nums)):
            if target-nums[i] in nums:
                my_dict[nums[i]]= target-nums[i]
                my_set.add(i)
                
        return list(my_set)
       
    


s=Solution()
nums=[2,7,11,15]
target=18
print(s.twoSum(nums,target))
        
    
