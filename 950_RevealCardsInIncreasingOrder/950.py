'''�Լ��Ĵ���'''
'''
    ��ʵ���ǰ�sotred�õ����ݰ�˳������һ���µ�������
    ����ͣ�����ֵ��Ӧ������Ϊ��ʱ����һ������������λ�ã��������ݡ�
    ��һ��label����Ǹ�����ֵ�Ƿ��Ѿ��������ݡ�
    �����λ��ȫ����1������ ѭ����
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