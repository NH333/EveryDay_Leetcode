'''我的想法'''
'''
    最近又在看滑动窗口的论文，然后可以把这个k想成窗口长度。
    貌似没啥用，因为时间限制没通过。就是注释部分的求和过程，还可以改进。
    然后，就是不需要每次都用sum把新的窗口里面的四个值都求和，
    因为每次滑动窗口，sum变成了 ： 原来sum - 原窗口第一个值 + 现窗口最后一个值。
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        slid_window = k
        # sum_slid_window = len(nums)-k+1
        # max_average = sum(nums[0:slid_window])/slid_window
        max_sum,tmp_sum = sum(nums[0:slid_window]),sum(nums[0:slid_window])
        # tmp_average = 0
        # tmp_sum = 0
        for i in range(slid_window,len(nums)):
            tmp_sum = tmp_sum + nums[i] - nums[i-slid_window]
            # tmp_average = sum(nums[i:i+slid_window])/slid_window
            if tmp_sum > max_sum:
                max_sum = tmp_sum
        
        return max_sum/slid_window