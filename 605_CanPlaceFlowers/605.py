'''�Լ��Ĵ���'''
'''
    �뷨���ǣ���������0��ͳ�Ƴ���������һ�Σ�Ȼ������һ�Ρ�
    ���������߽����⣬����00100�������������Ҫ�ֿ�����
    1.��ͷ��00�Ľ���취�Ƚϼ�
    2.�����00�Ľ���취���ǣ������鷴ת����������һ��1��λ�á�
    
    Ȼ����������ۡ�
    
    �������ȫΪ0�����������collections��Counter�������

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



'''�������'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if n == 0:
            return True
        else:
            newbed = [0]+flowerbed+[0]     #������ǰ���0        
            for i in range(1,len(newbed)-1):
                if newbed[i] == 0 and newbed[i-1]== 0 and newbed[i+1] == 0: #3��������0��һ��ͳ�ƣ�Ȼ����м��0��ֵΪ1
                    newbed[i] = 1
                    n -= 1                                                  #ÿһ������һ�仨��n�ͼ�ȥ1������Ҫ�����еĽ����ͳ�Ƴ�����
                    if n == 0:
                        return True
                    
            return False