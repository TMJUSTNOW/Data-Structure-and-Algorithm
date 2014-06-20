#!/usr/bin/env python
# -*- coding:utf-8 -*-

def maxHeap(l, start_index, end_index):
    root = start_index
    while start_index<=end_index:
        child = root*2 + 1
        if child > end_index:
            break
        if child+1 <= end_index and l[child] < l[child+1]:
            child += 1
        if l[root] < l[child]:
            temp = l[root]
            l[root] = l[child]
            l[child] = temp

            root = child
        else:
            break

def heapSort(l):
    for start in range(len(l)/2,-1,-1):
        maxHeap(l, start, len(l)-1)

    for end in range(len(l)-1,0,-1):
        temp = l[end]
        l[end] = l[0]
        l[0] = temp
        maxHeap(l,0,end-1)
        print l

    return l

if __name__ == '__main__':
    l = [8,10,4,5,3,1,11,6,13,5]
    l = heapSort(l)
    print l
