'''这题比较简单，直接上代码，不多比比'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        result = []
        for key in count:
            if count[key] == 2:
                result.append(key)
        
        return sorted(result)

'''set()函数的用法，去掉重复'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        found = set()
        for num in nums:
            if num in found:
                duplicates.append(num)
            found.add(num)
        return duplicates