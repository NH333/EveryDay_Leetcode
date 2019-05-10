class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = 0
        tmpSub = 0
        for i in range(len(nums)):
            tmpSub = tmpSub + nums[i]
            if(tmpSub > maxSub):
                maxSub = tmpSub
            elif(tmpSub < 0):
                tmpSub = 0
        
        '''��֤��Ϊ����������'''        
        if maxSub == 0:
            return max(nums)
        else:
            return maxSub