'''我的想法'''
'''
    先考虑中间的情况就是大于等于两个1出现的情况
    然后两端为0的情况分开讨论
    submission了好多次，难受呀！
'''
def maxDistToClosest(seats):
        index_left = 0
        index_raght = 0
        count = 1                               #count为1表示第一次出现1；为2表示第二次出现了1
        flag = 0                                #当两次出现1时，进入flag
        max_distance = 0
        max_index = 0
        tmp_distance = 0
        result = 0
        for i in range(len(seats)):
            if seats[i] == 1 and count == 1:  #定位第一次出现1
                index_left = i
                count += 1
                continue
                
            if seats[i] == 1 and count == 2:  #定位第二次出现1
                index_right = i
                count = 1
                flag = 1
                # index_left = index_right
            
            if flag:                           #当两次出现1之后，进入flag
                mid = (index_left + index_right)//2
                if seats[mid] == 1:            #判断 如果是两个相邻的1，则continue，并把rleft的1更新为right的1的位置
                    index_left = index_right
                    count = 2
                    flag = 0
                    continue
                else:                          #否则计算距离
                    # tmp_distance = (mid-index_left)**2 + (mid-index_right)**2
                    tmp_distance = abs(mid-index_left)
                    if tmp_distance >= max_distance: #判断距离是否比之前的大
                        max_distance = tmp_distance
                        max_index = mid
                        
                    # index_left = index_right
                        result = min(abs(max_index - index_left),abs(max_index - index_right))

                    index_left = index_right        #更新left的1的位置
                    count = 2                       
                    flag = 0
       
        '''起始为0的情况'''
        if seats[0] == 0:
            for i in range(len(seats)):
                if seats[i] == 1:
                    tmp_distance = i
                    if tmp_distance > max_distance:
                        max_distance = tmp_distance
                        # max_index = 0
                        result = max_distance
                    break
            # tmp_distance = index_left**2
            # if tmp_distance > max_distance:
            #     max_distance = tmp_distance
            #     max_index = 0
            #     result = abs(max_index - index_left)
        '''末端为0的情况'''
        if seats[-1] == 0:
            tmp_seats = seats[::-1]
            for i in range(len(tmp_seats)):
                if tmp_seats[i] == 1:
                    tmp_distance = i
                    if tmp_distance > max_distance:
                        max_distance = tmp_distance
                        # max_index = 0
                        result = max_distance
                    break
            # if tmp_distance > max_distance:
            #     max_distance = tmp_distance
            #     max_index = len(seats)-1
            #     result = abs(max_index - index_left)
                
        return result  

'''测试'''
a = [1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1]
b = maxDistToClosest(a)


'''优秀代码'''
'''
    思路清晰啊，相见恨晚啊，我好笨啊！
'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev, result = -1, 1
        for i in range(len(seats)):
            if seats[i]:              #判断是否为1
                if prev < 0:          #prev用来存储前一个1的位置，如果之前都没有1，就把结果赋值给现在1出现的位置，很好理解
                    result = i
                else:                 #如果之前存过1，i表示当前出现1的位置，然后比较最大的距离
                    result = max(result, (i-prev)//2)
                prev = i
        return max(result, len(seats)-1-prev)


input('')