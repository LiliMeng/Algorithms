# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Brute-force O(n^2)
class Solution1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        res = 0
        for i in range(length):
            for j in range(length):
                if i > j:
                   tmp_area = min(height[i],height[j])*(i-j)
                   if tmp_area > res:
                       res = tmp_area
                       
        return res
                   
#Two pointers O(n)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) -1 
        res = 0 
        
        while(left<right):
            tmp = min(height[left], height[right])*(right-left)
            res = max(tmp, res)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return res                

height = [1,3,2,4]

sol = Solution()
print(sol.maxArea(height))

