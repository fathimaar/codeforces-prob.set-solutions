#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:54:39 2022

@author: fathimaabdulrahman
"""

def diff_op():
    n = int(input())
    array = list(map(int,input().split()))
    first = array[0]
    call = []
    for i in array[1:]:
        if i%first == 0 and i>=first:
            call.append(1)
        else:
            call.append(0)
    if 0 in call: 
        print('no')
    else:
        print('yes')
    
if __name__ == "__main__":
    for case in range(int(input())):
        diff_op()
            