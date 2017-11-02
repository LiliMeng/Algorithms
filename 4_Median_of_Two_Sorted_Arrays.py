class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mergedList=nums1+nums2
        mergedList.sort()
        l = len(mergedList)
        if l%2==0:
            return float(mergedList[l/2-1]+mergedList[l/2])/2
        else:
            return float(mergedList[l/2])
        
