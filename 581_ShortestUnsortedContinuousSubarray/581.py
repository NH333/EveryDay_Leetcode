'''自己的代码'''
'''
    超时了，最近不知道为啥，特别想用迭代，也不知自己懂不懂迭代，很迷醉。
    然后就超时了，c了2/3.
    思路就是：从两端开始逼近，逐渐缩小数组。
    最后返回不能再缩进的数组的长度。
'''
def findUnsortedSubarray( nums) :
        if nums[0] == min(nums) and nums[-1] == max(nums):
            nums[:] = nums[1:len(nums)-1]
            return findUnsortedSubarray(nums)
        else:
            if nums[0] == min(nums):
                return findUnsortedSubarray(nums[1:])
            elif nums[-1] == max(nums):
                return findUnsortedSubarray(nums[:len(nums)-1])
            else:
                return len(nums)
            
findUnsortedSubarray(a)
input('')

'''优秀代码'''
'''
    思路很简单：先把数组排序sorted()
    然后对比原数组，哪个位置的值没对应上就存储下来
    最后返回索引值的差值+1.
    遍历了一遍。
'''
def findUnsortedSubarray( nums) :
    sort = sorted(nums)
            x = []
            for i in range(len(nums)):
                if nums[i] != sort[i]:
                    x.append(i)
            if not x:
                return 0
            else:
                return x[-1]-x[0]+1

'''优秀代码'''
'''
    思路：前两次while是为了找到不递增的子序列。if是为了判断如果时刚好递增或者空列表，及返回0
    后两个while是为了测试下面这种情况[2,4,6,3,8,10,9,15].注意这个3，其实就是为了把3往前挪几个位置，后面也同理。
'''
def findUnsortedSubarray(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j and nums[i] <= nums [i+1]: i += 1
        if i >= j:
            return (0)
        while j > 0 and nums[j] >= nums[j-1]: j -= 1

        max_sub, min_sub = max(nums[i:j+1]), min(nums[i:j+1])

        while i >= 0 and nums[i] > min_sub: i -= 1

        while j <= len(nums) - 1 and  nums[j] < max_sub: j += 1

        return(j-i-1)