'''����Ƚϼ򵥣�ֱ���ϴ��룬����ȱ�'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        result = []
        for key in count:
            if count[key] == 2:
                result.append(key)
        
        return sorted(result)

'''set()�������÷���ȥ���ظ�'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        found = set()
        for num in nums:
            if num in found:
                duplicates.append(num)
            found.add(num)
        return duplicates