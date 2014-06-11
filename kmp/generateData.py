#!/usr/bin/env python
# -*- coding:utf-8 -*-

from random import sample
from string import ascii_letters, digits

def getString():
    n = 1000000
    origin_str = ''
    while(n):
        tmp = ''.join(sample(ascii_letters + digits, 10))
        origin_str += tmp
        print "origin_str is %s",origin_str
        n -= 1
    origin_str += "abcdabd"
    return origin_str


if __name__ == '__main__':
	file_longstr = open('data_str','w')
	file_longstr.write(getString())
	file_longstr.close()
