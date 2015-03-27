#!/usr/bin/env python
# -*- coding:utf-8 -*-
''' 快速排序的原理是将取出第一个数，将整个数组分为两波，一拨都大于这个数，
另一波都小于这个数，然后递归用同样的方法处理第一波数字和第二波数字。
都说是“快速排序”，效率肯定比其他的一般排序算法高.'''

import random
def quicksort(L):
    if len(L) > 1:
        pivot = random.randrange(len(L))
        elements = L[:pivot]+L[pivot+1:]
        left  = [element for element in elements if element < L[pivot]]
        right =[element for element in elements if element >= L[pivot]]
        return quicksort(left)+[L[pivot]]+quicksort(right)
    return L

alist = [54,26,93,17,77,31,44,55,20]
print quicksort(alist)
