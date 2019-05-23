'''自己的想法'''
'''
    就是从两边开始找到非递增的位置i和j，通过i就是j的邻居，我们就可以ac过很多情况，但是最后还是想不到怎么解决所i有的情况。
    在[3,4,2,3]和[1,3,5,2,4]栽了跟头，想不出解决办法。
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums_copy = nums.copy()
        tmp = 0
        i,j = 0, len(nums)-1
        min_sub = 0
        max_sub = 0
        if len(nums) <= 2:
            return True
        
        while i<j and nums[i] <= nums[i+1] : i += 1
        if i>=j:
            return True
        while j>0 and nums[j] >= nums[j-1] : j -= 1
        if i+1 != j:
            return False
        else:
            if i == 0 or j==len(nums)-1:
                return True
            else:
                min_sub2 = min(nums[j:])
                min_sub1 = min(nums[:i+1])
                max_sub2 = max(nums[j:])
                max_sub1 = max(nums[:i+1])
                
                if min_sub1 <= min_sub2 :
                    return True
                else:
                    return False

'''参考别人的想法'''
'''
    修改最后的约束，就是把i和j两个位置的值，一次全取i位置的值，一次全取j位置的值，然后进行sorted排序，满足其中一种情况就是True。
    虽然，不知道怎么证明，但是好有道理的样子。然后我在想为啥不能直接del删除掉，然后想到3个数的时候，删掉都成立。所以不能直接删除。
    至于优秀代码，还没看懂。。。
'''          
            
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums_copy = nums.copy()
        tmp = 0
        i,j = 0, len(nums)-1
        sub1 = nums.copy()
        sub2 = nums.copy()
        if len(nums) <= 2:
            return True
        
        while i<j and nums[i] <= nums[i+1] : i += 1
        if i>=j:
            return True
        while j>0 and nums[j] >= nums[j-1] : j -= 1
        if i+1 != j:
            return False
        else:
            if i == 0 or j==len(nums)-1:
                return True
            else:
                '''-----------------------------核心-----------------------------'''
                sub1[i] = nums[j]
                sub2[j] = nums[i]
                
                if sub1 == sorted(sub1) or sub2 == sorted(sub2) :
                    return True
                else:
                    return False
                '''-----------------------------核心-----------------------------'''


'''优秀代码'''
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = None
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i
                
        return (
            p is None or
            p == 0 or
            p == len(nums) -2 or
            nums[p-1] <= nums[p+1] or
            nums[p] <= nums[p+2]
        )