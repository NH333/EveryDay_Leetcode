'''我的想法'''
'''
    用差值比较，当差值小于等于0的时候就返回索引值，
    如果循环结束diff还大于0，则返回最后的索引值+1
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        diff = 0
        min_value = target - nums[0]
        min_num = 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff <= min_value:
                min_value = diff
                min_num = i
                if min_value <= 0:
                    return min_num
        return min_num


'''优秀代码'''
'''
    二分查找
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low, high = 0, len(nums) - 1
        
        while low <= high:   #当low > high时，则退出while循环 验证的是插入元素不在列表里的情况
            mid = (low + high) // 2
            
            if nums[mid] == target:  #好理解
                return mid
            
            elif nums[mid]>target:
                high = mid - 1
                
            else:
                low = mid + 1
                
        
        return low