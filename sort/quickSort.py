#!/usr/bin/env python
# -*- coding:utf-8 -*-

def swap(arr, pre_idx, lat_idx):
    tmp = arr[pre_idx]
    arr[pre_idx] = arr[lat_idx]
    arr[lat_idx] = tmp

def getMiddleIndex(l, start_index, end_index):
    flag = l[end_index]
    i = start_index - 1
    for j in range(start_index, end_index):
        if l[j] > flag:
            pass
        else:
            i += 1
            swap(l, i, j)
    i += 1
    swap(l, i, end_index)
    return i

def quickSort(l, start_index, end_index):
    if start_index >= end_index:
        return
    middle = getMiddleIndex(l, start_index, end_index)
    print l
    quickSort(l,start_index, middle-1)
    quickSort(l, middle+1, end_index)

if __name__ == '__main__':
    l = [8,10,4,5,3,1,11,6,13,5]
    l = [8, 10, 4, 5, 3]
    quickSort(l, 0, len(l)-1)
    print l
