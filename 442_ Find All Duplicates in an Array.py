#442. Find All Duplicates in an Array
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    #Sign
        res=[]
        for n in nums:
            if nums[abs(n)-1]<0:
                res.append(abs(n))
            else:
                nums[abs(n)-1]*=-1
        return res