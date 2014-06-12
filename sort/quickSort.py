#!/usr/bin/env python
# -*- coding:utf-8 -*-

def getMiddleIndex(l, start_index, end_index):
    flag = l[end_index]
    i = start_index - 1
    for j in range(start_index, end_index):
        if l[j] > flag:
            pass
        else:
            i += 1
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
    i += 1
    tmp = l[end_index]
    l[end_index] = l[i]
    l[i] = tmp

    return i

def quickSort(l, start_index, end_index):
    if start_index >= end_index:
        return
    middle = getMiddleIndex(l, start_index, end_index)
    quickSort(l,start_index, middle-1)
    quickSort(l, middle+1, end_index)
    print l


if __name__ == '__main__':
    l = [8,10,4,5,3,1,11,6,13,5]
    quickSort(l, 0, len(l)-1)
    print l
