'''�Լ��Ĵ���'''
'''
    ��ʱ�ˣ������֪��Ϊɶ���ر����õ�����Ҳ��֪�Լ�������������������
    Ȼ��ͳ�ʱ�ˣ�c��2/3.
    ˼·���ǣ������˿�ʼ�ƽ�������С���顣
    ��󷵻ز���������������ĳ��ȡ�
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

'''�������'''
'''
    ˼·�ܼ򵥣��Ȱ���������sorted()
    Ȼ��Ա�ԭ���飬�ĸ�λ�õ�ֵû��Ӧ�Ͼʹ洢����
    ��󷵻�����ֵ�Ĳ�ֵ+1.
    ������һ�顣
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

'''�������'''
'''
    ˼·��ǰ����while��Ϊ���ҵ��������������С�if��Ϊ���ж����ʱ�պõ������߿��б�������0
    ������while��Ϊ�˲��������������[2,4,6,3,8,10,9,15].ע�����3����ʵ����Ϊ�˰�3��ǰŲ����λ�ã�����Ҳͬ��
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