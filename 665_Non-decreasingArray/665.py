'''�Լ����뷨'''
'''
    ���Ǵ����߿�ʼ�ҵ��ǵ�����λ��i��j��ͨ��i����j���ھӣ����ǾͿ���ac���ܶ����������������벻����ô�����i�е������
    ��[3,4,2,3]��[1,3,5,2,4]���˸�ͷ���벻������취��
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

'''�ο����˵��뷨'''
'''
    �޸�����Լ�������ǰ�i��j����λ�õ�ֵ��һ��ȫȡiλ�õ�ֵ��һ��ȫȡjλ�õ�ֵ��Ȼ�����sorted������������һ���������True��
    ��Ȼ����֪����ô֤�������Ǻ��е�������ӡ�Ȼ��������Ϊɶ����ֱ��delɾ������Ȼ���뵽3������ʱ��ɾ�������������Բ���ֱ��ɾ����
    ����������룬��û����������
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
                '''-----------------------------����-----------------------------'''
                sub1[i] = nums[j]
                sub2[j] = nums[i]
                
                if sub1 == sorted(sub1) or sub2 == sorted(sub2) :
                    return True
                else:
                    return False
                '''-----------------------------����-----------------------------'''


'''�������'''
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