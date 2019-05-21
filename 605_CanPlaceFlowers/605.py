'''自己的代码'''
'''
    想法就是，把连续的0的统计出来，计算一次，然后重置一次。
    但是遇到边界问题，遇到00100，这种情况，就要分开讨论
    1.开头的00的解决办法比较简单
    2.后面的00的解决办法就是，把数组反转，计算出最后一个1的位置。
    
    然后分三段讨论。
    
    最后遇到全为0的情况，利用collections的Counter方法解决

'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count_zero = 0
        count_num = 0
        last_one = 0
        count_all = collections.Counter(flowerbed)
        if count_all[1] == 0:
            return ((count_all[0]+1)//2) >= n
        
        flowerbed_oppsite = flowerbed[::-1]
        
        for i in range(len(flowerbed_oppsite)):
            if flowerbed_oppsite[i] == 1:
                last_one = i
                break
                
        last_one = len(flowerbed) - last_one -1
        
        if flowerbed[0] == 0:
            count_zero = 2
        
        for i in range(1,last_one+1):
            if flowerbed[i] == 0 :
                count_zero += 1
                # continue
                # count_num += count_zero // 2
                
            elif count_zero > 2:
                count_num += (count_zero-1) // 2
                count_zero = 0
            else:
                count_zero = 0
                continue
        
        count_zero = collections.Counter(flowerbed[last_one:])
        count_num += count_zero[0] // 2
            
        
        
        if count_num >= n:
            return True
        else:
            return False



'''优秀代码'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if n == 0:
            return True
        else:
            newbed = [0]+flowerbed+[0]     #把数组前后加0        
            for i in range(1,len(newbed)-1):
                if newbed[i] == 0 and newbed[i-1]== 0 and newbed[i+1] == 0: #3个连续的0做一个统计，然后把中间的0赋值为1
                    newbed[i] = 1
                    n -= 1                                                  #每一次种上一朵花，n就减去1，不需要把所有的结果都统计出来。
                    if n == 0:
                        return True
                    
            return False