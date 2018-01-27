class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        curSub = maxSub = nums[0]
        for num in nums[1:]:
            curSub = max(curSub+num, num)
            maxSub = max(maxSub, curSub)
            
        return maxSub
