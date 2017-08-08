class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            L, R = i + 1, n - 1
            while L < R:
                temp = nums[i] + nums[L] + nums[R]
                if temp == 0:
                    ans.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]: L += 1
                    while R > L and nums[R] == nums[R + 1]: R -= 1
                elif temp > 0:
                    R -= 1
                else:
                    L += 1
        return ans

