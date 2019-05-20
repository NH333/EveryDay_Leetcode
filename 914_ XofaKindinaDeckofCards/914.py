#!/usr/bin/python
# -*- coding: utf-8 -*-       
#coding=utf-8
# coding: unicode_escape

'''自己的方法，没通过，当每个数字的统计之和为奇数的时候，挂掉了。'''
'''
    利用递归的方法，就是遇到一样的数字，就删除掉。如果数组最后变成空，那么就是符合条件的。但是没想到奇数的情况。
    中间遇到一些问题，就是递归的使用，没有在递归函数前加return 就出现了别的问题，折腾好久。
    然后，还研究了一下深拷贝，和浅拷贝。
    能记得就是，数字，字符串，元组，作为参数传递，就是值传递，不会被修改。
    像列表，字典作为参数传递的时候，它们在函数执行后原来的也会被修改。
'''
class Solution:
    def hasGroupsSizeX(self, deck):
        if deck == []:
            return True
        else:
            for i in range(1,len(deck)):

                if deck[i] == deck[0]:
                    del deck[i]
                    del deck[0]
                    return self.hasGroupsSizeX(deck)
                    
            return False

'''
    优秀代码
    学习到了collections库，leetcode上可以直接用

    collections模块自Python 2.4版本开始被引入，包含了dict、set、list、tuple以外的一些特殊的容器类型，分别是：

    OrderedDict类：排序字典，是字典的子类。引入自2.7。
    namedtuple()函数：命名元组，是一个工厂函数。引入自2.6。
    Counter类：为hashable对象计数，是字典的子类。引入自2.7。
    deque：双向队列。引入自2.4。
    defaultdict：使用工厂函数创建字典，使不用考虑缺失的字典键。引入自2.5。
    http://www.pythoner.com/205.html
'''
import collections
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        count = collections.Counter(deck)  #count 就是一个字典key就是对应的数字，value对应的就是统计出来的值。
        X = min(count.values())
        for x in range(2, X + 1):
            if all(v % x == 0 for v in count.values()):  #所有数字的统计之和都能被 最小的统计之和 整除 就是满足题目条件！ 强！ 无敌！
                return True
        return False

deck = [1,2,3,4,4,3,2,1]
a = Solution()
a.hasGroupsSizeX(deck)
input('')