class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
       
        res=[]
        my_dict={}   
        
        for i in range(len(nums)):
          for j in range(len(nums)):
              if (-nums[i]-nums[j]) in nums:
                  k=nums.index(-nums[i]-nums[j])
                  my_dict[nums[i]+nums[j]]=-nums[i]-nums[j]
                  if(i!=j and i!=k and j!=k):
                      single_res=[]
                      single_res.append(nums[i])
                      single_res.append(nums[j])
                      single_res.append(-nums[i]-nums[j])
                      single_res.sort()
                      res.append(single_res)
                      
              
    
        return list(set(map(tuple,res)))
    
s=Solution()
nums=[-1, 0, 1, 2, -1, -4]
res=s.threeSum(nums)
print(len(res))
print(res)
