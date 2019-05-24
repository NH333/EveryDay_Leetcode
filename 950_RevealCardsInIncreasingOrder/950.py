'''自己的代码'''
'''
    其实就是把sotred好的数据按顺序填入一个新的数组里
    规则就，索引值对应的内容为空时，隔一个这样的索引位置，填入数据。
    用一个label来标记该索引值是否已经填入内容。
    当标记位置全填满1后跳出 循环。
'''
def deckRevealedIncreasing(deck):
        deck = sorted(deck)
        result = [0] * len(deck)
        index_label = [0]*len(deck)
        # index_result = [1]*len(deck)
        result[0] = deck[0]
        index_label[0] = 1
        # count_True = 1
        tmp_count_True = 0
        j=1
        while sum(index_label) != len(deck):
            for i in range(1,len(deck)):
                if index_label[i] == 1:
                    continue
                else:
                    tmp_count_True += 1
                
                if tmp_count_True == 2:
                    index_label[i] = 1
                    result[i] = deck[j]
                    j += 1
                    tmp_count_True = 0
                    
        
        return result
a = [17,13,11,2,3,5,7]
deckRevealedIncreasing(a)
input('')