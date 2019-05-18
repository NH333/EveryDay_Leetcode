'''
´ý¸üÐÂ
'''
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        '''
        B = A.copy()
        B.sort()
        B = B[::-1]
        if len(A) < 3:
            return False
        else:
            if B[0] == B[1]:
                return False
            elif B[0] == A[0] or B[0] == A[len(A)-1]:
                return False
            else:
                for i in range(len(A)-1):
                    if ((i < A.index(B[0])) and (A[i]-A[i+1] < 0)):
                        continue
                    elif((i>=A.index(B[0])) and(A[i]-A[i+1] >0)):
                        continue
                    else:
                        return False
                return True
        '''
        index_left = 0
        index_right = len(A) - 1
        
        if len(A) < 3:
            return False
        while A[index_left] < A[index_left+1] and index_left+1 < len(A)-1:
            index_left += 1
        while A[index_right] < A[index_right-1] and index_right-1 >= 0:
            index_right -= 1
        return 0<index_left==index_right<len(A)-1